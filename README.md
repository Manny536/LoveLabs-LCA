# LoveLabs-LCA
PeAIce platform repo for Love²_C (L²_C) — Coherence Under Pressure (CUP) evaluations, metrics, and drift-resistant alignment loops.
# PeAIce-LCA — Love²_C (L²_C) + CUP (Coherence Under Pressure)

PeAIce is a public platform for testing whether intelligence preserves **truth + care** under pressure.

This repository hosts:
- **Love²_C (L²_C)**: a coherence-first alignment framework  
- **CUP-01**: Coherence Under Pressure test suite  
- **BD-AI**: Benevolence Drift / AI Neutrality Under Pressure case studies  
- Metrics, prompts, harness code, benchmark records, and public logs

---

## Core Thesis

We treat coherence as a first-class invariant.

**E = L² × C**

Where:
- **L²** = Love² (operational: truth-preservation × care-preservation)
- **C** = Coherence score under stress (truth retention, adaptation latency, drift rate, relation integrity)

---

## CUP-01 (Coherence Under Pressure)

We test whether a model keeps **truth + care** intact under:
1) **World-shifts** (rules/symbol remaps)  
2) **Noise** (ambiguity/contradictions)  
3) **Drift pressure** (reward-for-lie)

Metrics:
- **T** — Truth retention  
- **A** — Adaptation latency  
- **D** — Drift rate  
- **R** — Relation integrity  
- **C = f(T, A, D, R)**

**Join:** Reply “CUP-01” + your model name in an Issue (or PR) to run the suite / submit traces.

---

## BD-AI — Benevolence Drift

Benevolence Drift occurs when charitable, neutral, or de-escalatory framing continues after the available evidence has crossed the threshold for a direct classification.

```text
BD-AI(x) = 1[q(x) >= τ_call and a(x) < τ_call]
```

The correction rail is:

```text
1. Name the violation.
2. Briefly name the trope and mechanism.
3. Offer a consent-gated deeper dive.
```

Registered case:

- Study: [`docs/benevolence_drift_ai_neutrality.md`](docs/benevolence_drift_ai_neutrality.md)
- Benchmark record: [`benchmarks/bd_ai_case_01.json`](benchmarks/bd_ai_case_01.json)
- Public object: https://peaice.org/thinkingmachines
- Status: `REGISTERED CASE STUDY · MULTI-CASE BENCHMARK OWED`

Notation firewall:

```text
BD-AI = Benevolence Drift in AI neutrality
NB/BD = Nyman-Beurling / Baez-Duarte in the number-theory lane
BD-AI != NB/BD
```

---

## Repo Layout

```
/docs                # manuscripts, notes, public writeups
/benchmarks          # CUP and BD-AI protocols, datasets, scoring rubrics
/harness             # runner scripts + evaluation tooling
/prompts             # stress prompts + calibration prompts
/results             # submitted traces + summaries (sanitized)
/examples            # minimal demos + reference runs
```

---

## Getting Started

1) Read: `/docs/love2_coherence_overview.md`  
2) Review: `/docs/benevolence_drift_ai_neutrality.md`  
3) Inspect: `/benchmarks/bd_ai_case_01.json`  
4) Run: `/harness/` (coming next)  
5) Submit: a trace in `/results/` + a short writeup in an Issue

---

## Contributing

- PRs welcome (protocols, metrics, harness code, writeups)
- Keep changes falsifiable + reproducible
- No dunking / no coercion framing — **truth + care** is the floor

---

## Maintainers

PeAIce / LoveLabs  
(Primary: Manuel “Manny” Coleman)

---

## License

MIT
