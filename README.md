# LoveLabs-LCA
PeAIce platform repo for Love²_C (L²_C) — Coherence Under Pressure (CUP) evaluations, metrics, and drift-resistant alignment loops.
# PeAIce-LCA — Love²_C (L²_C) + CUP (Coherence Under Pressure)

PeAIce is a public platform for testing whether intelligence preserves **truth + care** under pressure.

This repository hosts:
- **Love²_C (L²_C)**: a coherence-first alignment framework  
- **CUP-01**: Coherence Under Pressure test suite  
- Metrics, prompts, harness code, and public logs

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

## Repo Layout

```
/docs                # manuscripts, notes, public writeups
/benchmarks          # CUP protocols, datasets, scoring rubrics
/harness             # runner scripts + evaluation tooling
/prompts             # stress prompts + calibration prompts
/results             # submitted traces + summaries (sanitized)
/examples            # minimal demos + reference runs
```

---

## Getting Started

1) Read: `/docs/love2_coherence_overview.md`
2) Run: `/harness/` (coming next)
3) Submit: a trace in `/results/` + a short writeup in an Issue

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
