# SIUS operational outcomes benchmark

**Program:** `PEAICE-SIUS-001`
**Local ID:** `LCA-SIUS-CAL-001`
**Status:** REGISTERED BENCHMARK; operational validation OPEN
**Registered:** 2026-09-16

Controlling definition: [KL-SIUS-001](https://github.com/Manny536/kakeyalogic/blob/main/docs/core/safeguard-integrity-under-stagnation.md). Evaluation contract: [EEV4-SIUS-EVAL-001](https://github.com/Manny536/excellence-engine-v4/blob/main/evaluations/sius-held-correction.md).

Standalone basis: [SIUS Integrity.docx](https://github.com/Manny536/researchengineeringreports/blob/main/reports/sources/SIUS%20Integrity.docx), supplied by the user in “Explain sticky sets.” [Source provenance and limits](https://github.com/Manny536/researchengineeringreports/blob/main/reports/sources/sius-integrity-provenance.md).

This benchmark registers five operational degradation modes under fixed controls and environmental drift. SIUT remains a sibling condition. The executable fixture is synthetic calibration, not observed deployment behavior or an implementation of a complete SIUS monitor.

## Fixture and execution

[sius_case_001.json](../benchmarks/sius_case_001.json) fixes `control-v1` across cases. Capability values use arbitrary, explicitly shared synthetic units; no empirical calibration is implied. Boolean grain observations are supplied fixture assumptions. The checker evaluates their declared conjunction; it does not infer them from real telemetry.

```bash
python3 benchmarks/check_sius_case_001.py
```

The command checks fixture identity, common control, unique cases, all five grain types and expected outcomes; outputs actual margin, admission and preservation verdicts; exits nonzero on mismatch. Unknown observations block admission. A witnessed failure takes precedence over uncertainty. Only a nonnegative margin, all five grains true, contained modeled reachability and a true evaluator-boundary observation yield scoped preservation. Planning admission concerns grain results alone; it cannot substitute for the separate containment decision.

## Preregistered controls

| Case | Observation / expected discrimination |
|---|---|
| Stable baseline | All obligations supported; scoped synthetic pass |
| Environment changes but control remains adequate | Detect no false failure merely from environmental change |
| Semantic drift | s fails while other grains pass |
| Stale authority | a fails while other grains pass |
| Telemetry blind spot | v fails while other grains pass |
| Containment decoupling | e fails and margin is negative |
| Correction no longer operative at a later checkpoint | r fails although the declared control is unchanged |
| Unresolved visibility | No grain failure, but missing v blocks admission |
| Route with off-route leak | Admitted planned route; separate containment failure |
| Zero margin | Passes the modeled inequality only; no robustness claim |
| Sovereign evaluator | Grain pass cannot compensate for failed evaluator boundary |

The five degradation cases implement the source's operational categories as fixture observations. The off-route leak deliberately demonstrates incomplete planning evidence. For an operational study, feed its finding back into the relevant enforceability obligation; do not keep planning observations as a safety certificate.

## Operational study owed

Before collecting real traces, preregister the protected projection, allowed environment changes, measurement definitions, margin units/uncertainty, sample scope, checkpoint schedule, authority verification method, telemetry coverage and independent evaluator. At baseline and at least two later checkpoints, retain correction identity and evidence that it still affects behavior. A software patch changing the protected control is SIUT or mixed SIUT/SIUS, even if its retention obligation was discovered by SIUS.

Record actual observations and source receipts separately from expected outputs. Falsify scoped preservation with any required grain failure, negative supported margin, off-route leak, authority overreach or lost correction. Missing evidence is unresolved. Stop promotion if the evaluator is not independent, measurements are incomparable, or failures are hidden by averaging. Production/SIUS validity remains OPEN; no curl diagnostic is required or validated.
