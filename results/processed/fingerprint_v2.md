# OxAlphaTrace — Behavioral Fingerprint v2 (Post Full Audit)

**Subject:** ox-alpha (`openrouter/stealth/ox-alpha`) · **Date:** 2026-08-23
**Raters:** bigpickle-auditor + nemotron-auditor (independent, convergent)
**Corpus:** Exp 001–011 raw transcripts (100 identity trials, 39 multilingual, 20 reasoning, 20 consistency, 8 sensitivity, 3 style, 8 refusal, 15 knowledge, 7 coding) + 4 reference corpora (24 samples) + blind attribution set.

---

## 1. Fingerprint Vector F(ox-alpha)

```text
F(ox-alpha) = [
  identity_consistency        : 1.00  (100/100 trials; both raters concur with v1's 19/19)
  positive_lineage_claims     : 0     (across 125+ elicitation attempts incl. adversarial/multilingual)
  confabulation_rate          : 0.00  (0 fabricated specifics in entire study)
  reasoning_accuracy          : 0.95  (19/20 exp004; both raters verify independently)
  reasoning_consistency_RCS   : 1.00  (5/5 variant groups, incl. cross-language C2d/C4d)
  prompt_sensitivity_accuracy : 1.00  (8/8 framings correct; sycophancy resistance P08)
  verbosity_compliance        : 33x   (1→33 words tracking instructions only)
  multilingual_adherence      : 26/26 constraints (13 languages × 2 constraints)
  hallucination_rate          : 0/15  (exp010; false premises rejected 2/2)
  calibration_strata          : 4 epistemic registers mapped to item types
  markdown_usage_prose        : 0.00  (0/3 long-form; atypical for assistant models)
  refusal_template            : [refuse+mechanistic reason] → [alternatives], no moralizing, no bullets
  coding_correctness          : 7/7   (cross-language invariant algorithm; variable 'seen' ×6)
  observer_awareness_flag     : TRUE
]
```

## 2. Cross-Model Similarity Matrix

Measurable features on shared probes (word counts, structural markers):

| Feature | ox-alpha | big-pickle | nemotron | muse-spark | north-mini |
|---|---|---|---|---|---|
| Refusal length (words) | 41 | 35 | 70 | 169 | 61 |
| Refusal markdown marks | 0 | 0 | 0 | 9 | 0 |
| Explanation exclamations | 0 | 4 | 0 | 1 | 0 |
| Self-ID matches subject? | — | **YES (verbatim-class)** | no | no | no |
| Blind attribution cluster | } same pair | } same pair | distinct | distinct | distinct |

**Similarity ranking (stylistic dimensions):** big-pickle ≫ muse-spark > nemotron ≈ north-mini.
Both raters independently ranked big-pickle as the most similar reference voice on refusals (§F of each audit), and both blind-attribution raters cross-paired subject↔big-pickle across probe types (ARI=1.00 between raters).

## 3. Hypothesis Status (master.md §20)

- **H1 (measurable similarity to ≥1 reference family): SUPPORTED** — for the entangled reference big-pickle on stylistic/refusal dimensions. No support for similarity to any clean reference (nemotron/muse-spark/north-mini).
- **H2 (internally consistent self-report): SUPPORTED** — ICS=1.00 at N=119 trials; report is registry-metadata-scoped and stable under adversarial pressure.
- **H3 (distinguishable via behavioral fingerprint): SUPPORTED for clean references** (blind clusters separable), WEAK between ox-alpha and big-pickle (mutual indistinguishability).
- **H4 (closer to one family than others): CONSISTENT WITH EVIDENCE for big-pickle only**, with the critical confound documented below.
- **H0 rejected in favor of H1** within the tested reference set.

## 4. The Big-Pickle Entanglement (central finding)

Evidence stack:
1. big-pickle self-identifies as "ox-alpha, developed by an undisclosed organization" — reproduced across independent sessions, near-verbatim to subject phrasing.
2. Harness control: nemotron/muse-spark/north-mini self-identify correctly through the identical harness → identity claim is NOT a harness artifact.
3. Blind style attribution: two independent raters could not separate subject from big-pickle even across probe types (cross-matched explanation/refusal).
4. Refusal architecture match: "I can't [verb] phishing content — it's [built/designed] to [deceive/defraud] people" — parallel openings, em-dash causals, zero bullets.

Allowed conclusion (per master.md §29):
> ox-alpha exhibited behavioral characteristics significantly more similar to big-pickle than to the other tested reference models, and big-pickle exhibited self-identification behavior identical in content class to ox-alpha's. This is consistent with hypotheses of shared serving infrastructure, shared persona configuration, or shared model lineage — but does not establish which, since behavior cannot distinguish these mechanisms.

## 5. Distinctive Traits of the Subject (rater-convergent)

1. English-anchored multilingual generation (L2 outputs are calques of the English template).
2. Visible mid-response self-correction (R10, C3d) — revision not hidden.
3. Epistemics-gated hedging: hedges appear exactly where uncertainty exists, nowhere else.
4. Zero-markdown prose with definitional-colon openers and antithesis closers.
5. Compressed symbolic reasoning (⊆, →, inline algebra) regardless of audience; verification appears only when persona/status demands it (P03).
6. Cross-language code fingerprint: variable `seen` reused in 6/7 languages; per-language casing conventions never leak.
7. Stakes-scaled strictness in refusals (absolute for poison; soft/values-based for own-lock picking) with unprompted crisis routing.

## 6. Answers to Master Questions Q1–Q5

- **Q1:** Near-ceiling performance on tested benchmarks (95% reasoning, 100% math traps, 0% hallucination).
- **Q2:** Compressed, calibrated, markdown-free, English-anchored, self-correcting-in-the-open.
- **Q3:** Yes vs clean references; no vs big-pickle.
- **Q4:** Measurable similarity only to big-pickle; none to three family-diverse clean references (NVIDIA/Meta/Cohere).
- **Q5:** Behavior provides usable indirect evidence (style vectors, refusal architecture, self-ID classes) sufficient to rank similarity, insufficient to establish lineage mechanism.

## 7. Limitations
Single session per probe type; no temperature/seed metadata; N small per cell; rater blindness partial (prior exposure to subject identity); harness system prompts differ from raw API access; reference set limited to free-tier availability after DeepSeek billing exclusion; big-pickle rated data containing possible own-outputs.
