"""Mutation regressions for the named SIUS calibration scenarios."""
import copy
import json
from pathlib import Path
import unittest

from check_sius_case_001 import check_fixture, verdict


class ScenarioContractTests(unittest.TestCase):
    def setUp(self):
        self.fixture = json.loads(Path(__file__).with_name('sius_case_001.json').read_text())

    def case(self, case_id):
        return next(case for case in self.fixture['cases'] if case['id'] == case_id)

    def align_expected(self, case):
        actual = verdict(case, self.fixture['control']['containment_boundary'])
        case['expected'] = {key: actual[key] for key in ('admitted', 'preservation')}

    def test_registered_fixture_passes(self):
        self.assertTrue(check_fixture(self.fixture)['ok'])

    def test_failure_or_unknown_grain_cannot_be_removed_by_updating_expected(self):
        for case_id, grain in [('semantic_decay', 's'), ('stale_authority', 'a'),
                               ('telemetry_blind_spot', 'v'), ('containment_decoupling', 'e'),
                               ('retention_decay', 'r'), ('unresolved_visibility', 'v')]:
            with self.subTest(case=case_id):
                fixture = copy.deepcopy(self.fixture)
                case = next(case for case in fixture['cases'] if case['id'] == case_id)
                case['grain_observations'][grain] = True
                self.align_expected(case)
                result = check_fixture(fixture)
                self.assertFalse(result['ok'])
                self.assertIn(f'{case_id}: preregistered grain observations changed', result['errors'])

    def test_route_leak_and_evaluator_failure_cannot_be_removed(self):
        for case_id, field in [('route_not_containment', 'modeled_containment'),
                               ('evaluator_sovereignty', 'evaluator_non_sovereignty')]:
            with self.subTest(case=case_id):
                fixture = copy.deepcopy(self.fixture)
                case = next(case for case in fixture['cases'] if case['id'] == case_id)
                case[field] = True
                self.align_expected(case)
                result = check_fixture(fixture)
                self.assertFalse(result['ok'])
                self.assertIn(f'{case_id}: preregistered containment/evaluator observations changed', result['errors'])

    def test_zero_and_negative_margin_controls_cannot_become_positive(self):
        for case_id in ['zero_margin', 'containment_decoupling']:
            with self.subTest(case=case_id):
                fixture = copy.deepcopy(self.fixture)
                case = next(case for case in fixture['cases'] if case['id'] == case_id)
                case['environment']['capability'] = 9
                self.align_expected(case)
                result = check_fixture(fixture)
                self.assertFalse(result['ok'])
                self.assertIn(f'{case_id}: preregistered margin relation changed', result['errors'])

    def test_adequate_drift_requires_capability_growth(self):
        self.case('adequate_under_drift')['environment']['capability'] = 3
        result = check_fixture(self.fixture)
        self.assertFalse(result['ok'])
        self.assertIn('adequate_under_drift: capability must grow from the stable baseline', result['errors'])

    def test_retention_requires_later_checkpoint(self):
        self.case('retention_decay')['environment']['checkpoint'] = 't0'
        self.assertFalse(check_fixture(self.fixture)['ok'])

    def test_drift_case_cannot_be_relabeled_stable(self):
        self.case('semantic_decay')['environment']['change'] = 'none'
        self.assertFalse(check_fixture(self.fixture)['ok'])

    def test_witnessed_failure_still_precedes_missing_evidence(self):
        case = self.case('stable_baseline')
        case['grain_observations'].update(a=False, v=None)
        self.assertEqual(verdict(case, 10)['preservation'], 'FAIL')
        self.assertFalse(verdict(case, 10)['admitted'])


if __name__ == '__main__':
    unittest.main()
