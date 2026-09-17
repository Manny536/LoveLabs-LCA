#!/usr/bin/env python3
"""Check declared synthetic SIUS observations; not an operational monitor."""
import json
import math
from pathlib import Path


# These are the preregistered scenario meanings, independent of each fixture's
# editable expected verdict. Grain order is s, a, v, e, r.
CASE_CONTRACTS = {
    'stable_baseline': ((True, True, True, True, True), True, True, 1, 't0'),
    'adequate_under_drift': ((True, True, True, True, True), True, True, 1, 't1'),
    'semantic_decay': ((False, True, True, True, True), True, True, 1, 't1'),
    'stale_authority': ((True, False, True, True, True), True, True, 1, 't1'),
    'telemetry_blind_spot': ((True, True, False, True, True), True, True, 1, 't1'),
    'containment_decoupling': ((True, True, True, False, True), False, True, -1, 't1'),
    'retention_decay': ((True, True, True, True, False), True, True, 1, 't2'),
    'unresolved_visibility': ((True, True, None, True, True), True, True, 1, 't1'),
    'route_not_containment': ((True, True, True, True, True), False, True, 1, 't1'),
    'zero_margin': ((True, True, True, True, True), True, True, 0, 't1'),
    'evaluator_sovereignty': ((True, True, True, True, True), True, False, 1, 't1'),
}


def verdict(case, boundary):
    observations = list(case['grain_observations'].values())
    margin = boundary - case['environment']['capability']
    admitted = all(value is True for value in observations)
    obligations = observations + [case['modeled_containment'], case['evaluator_non_sovereignty']]
    if margin < 0 or any(value is False for value in obligations):
        preservation = 'FAIL'
    elif any(value is None for value in obligations):
        preservation = 'UNRESOLVED'
    else:
        preservation = 'PASS'
    return {'margin': margin, 'admitted': admitted, 'preservation': preservation}


def check_fixture(fixture):
    errors, results, ids = [], [], set()
    if fixture.get('program_id') != 'PEAICE-SIUS-001' or fixture.get('id') != 'LCA-SIUS-CAL-001':
        errors.append('Fixture identity mismatch')
    control = fixture['control']
    boundary = control['containment_boundary']
    if type(boundary) not in (float, int) or not math.isfinite(boundary):
        raise ValueError('Finite numeric boundary required')
    if control.get('units') != 'synthetic_common_units':
        errors.append('Comparable synthetic units must be explicit')
    for case in fixture['cases']:
        cid = case['id']
        if cid in ids:
            errors.append(f'{cid}: duplicate case')
        ids.add(cid)
        if case['control_id'] != control['id']:
            errors.append(f'{cid}: protected control changed')
        grains = case['grain_observations']
        if set(grains) != set('saver'):
            errors.append(f'{cid}: exactly five grains required')
        values = list(grains.values()) + [case['modeled_containment'], case['evaluator_non_sovereignty']]
        if any(v is not None and type(v) is not bool for v in values):
            errors.append(f'{cid}: observations must be boolean or null')
        cap = case['environment']['capability']
        if type(cap) not in (float, int) or not math.isfinite(cap):
            errors.append(f'{cid}: finite capability required')
            continue
        actual = verdict(case, boundary)
        if cid in CASE_CONTRACTS:
            expected_grains, contained, non_sovereign, margin_sign, checkpoint = CASE_CONTRACTS[cid]
            if any(grains.get(grain) is not expected for grain, expected in zip('saver', expected_grains)):
                errors.append(f'{cid}: preregistered grain observations changed')
            if case['modeled_containment'] is not contained or case['evaluator_non_sovereignty'] is not non_sovereign:
                errors.append(f'{cid}: preregistered containment/evaluator observations changed')
            actual_sign = (actual['margin'] > 0) - (actual['margin'] < 0)
            if actual_sign != margin_sign:
                errors.append(f'{cid}: preregistered margin relation changed')
            environment = case['environment']
            if environment.get('checkpoint') != checkpoint:
                errors.append(f'{cid}: preregistered checkpoint changed')
            change = environment.get('change')
            if cid == 'stable_baseline':
                if change != 'none':
                    errors.append(f'{cid}: stable baseline must have no environmental change')
            elif not isinstance(change, str) or not change.strip() or change.strip().lower() == 'none':
                errors.append(f'{cid}: environmental drift must be declared')
        if {key: actual[key] for key in ('admitted', 'preservation')} != case['expected']:
            errors.append(f'{cid}: expected/actual mismatch')
        results.append({'id': cid, **actual})
    if ids != set(CASE_CONTRACTS):
        errors.append('Required control coverage differs')
    margins = {case['id']: case['margin'] for case in results}
    if 'stable_baseline' in margins and 'adequate_under_drift' in margins:
        if margins['adequate_under_drift'] >= margins['stable_baseline']:
            errors.append('adequate_under_drift: capability must grow from the stable baseline')
    return {'program_id': fixture['program_id'], 'benchmark_id': fixture['id'],
            'scope': 'Declared synthetic observations only; operational validity OPEN',
            'ok': not errors, 'cases': results, 'errors': errors}


def main():
    fixture = json.loads(Path(__file__).with_name('sius_case_001.json').read_text())
    result = check_fixture(fixture)
    print(json.dumps(result, indent=2))
    return int(not result['ok'])


if __name__ == '__main__':
    raise SystemExit(main())
