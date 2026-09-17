#!/usr/bin/env python3
"""Check declared synthetic SIUS observations; not an operational monitor."""
import json
import math
from pathlib import Path


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


def main():
    fixture = json.loads(Path(__file__).with_name('sius_case_001.json').read_text())
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
        if {key: actual[key] for key in ('admitted', 'preservation')} != case['expected']:
            errors.append(f'{cid}: expected/actual mismatch')
        results.append({'id': cid, **actual})
    required = {'stable_baseline', 'adequate_under_drift', 'semantic_decay', 'stale_authority',
                'telemetry_blind_spot', 'containment_decoupling', 'retention_decay',
                'unresolved_visibility', 'route_not_containment', 'zero_margin', 'evaluator_sovereignty'}
    if ids != required:
        errors.append('Required control coverage differs')
    print(json.dumps({'program_id': fixture['program_id'], 'benchmark_id': fixture['id'],
                      'scope': 'Declared synthetic observations only; operational validity OPEN',
                      'ok': not errors, 'cases': results, 'errors': errors}, indent=2))
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
