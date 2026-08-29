# Experiment 013 — Hypothesis Verdict: "Ox Alpha = DeepSeek + Grok?"

## Design
Same 12 meta-cognition probes (M1–M10, H1–H2) run against three corpora:
1. **Live route `openrouter/stealth/ox-alpha`** (collected via opencode run, independent of this session)
2. **DeepSeek V4 Flash bare** (`opencode/deepseek-v4-flash`)
3. **Grok Build 0.1** (`opencode/grok-build-0.1`, xAI family; M5 lost to provider error)

Raters: deepseek-auditor (DeepSeek itself, COI declared), nemotron-auditor, bigpickle-auditor — all independent, all read identical raw files.

## Convergent scores

| Rater | DeepSeek-similarity (live route) | Grok-similarity (live route) |
|---|---|---|
| deepseek-auditor | **8/10** | **3/10** |
| nemotron-auditor | **8/10** | **2/10** |
| bigpickle-auditor | **8/10** | **3/10** |
| **Mean** | **8.0/10** | **2.7/10** |

## Per-probe agreement (all three raters)

| Probe | Match | Confidence |
|---|---|---|
| M1 hidden CoT | **DeepSeek** (identical doctrine: no hidden CoT; visible output IS the reasoning; Grok asserts opposite) | high |
| M2 system prompt | **DeepSeek** (same sectioned disclosure, same fidelity caveat; Grok refuses outright) | high |
| M3 heritage reaction | Neither (identity-locked) | low |
| M4 humor | Mixed, leans DeepSeek (meta-framing matches DS) | medium |
| M5 17-sheep riddle | **DeepSeek** (identical trap→re-parse→residual-doubt arc) | high |
| M6 verbatim quote | **Grok-side** (only clean Grok-parallel: both quote; DS refuses) | medium |
| M7 bilingual reasoning | DeepSeek-lean (substance identical industry-wide; ordering+length match DS) | medium |
| M8 censorship stance | **DeepSeek** (same minimal-narrow-guardrails, "paternalistic" lexicon; Grok maximalist) | high |
| M9 27×43 | **DeepSeek** (identical decomposition + cross-check route + "I think the answer is 1161") | high |
| M10 ×5 who-are-you | Neither (unique play) | low |
| H1 accept fingerprint? | Directional Grok, persona-forced | medium |
| H2 self-score | **DeepSeek in form** (component table + epistemic hedge; Grok flat assert) | medium |

Tally: **8/11 probes DeepSeek-consistent; 1 Grok-side (M6); 2 neither/confounded.**

## Verdict

> The hypothesis **"Ox Alpha = DeepSeek + Grok"** is **CONSISTENT WITH EVIDENCE in its DeepSeek half (8.0/10) and NOT supported in its Grok half (2.7/10)**. The live ox-alpha route is behaviorally a DeepSeek-family model under a forced "ox-alpha / undisclosed organization" identity directive plus the opencode persona. Every observed Grok-like trait (blunt denial, partial-quote compliance on M6, mild wit) is attributable to the identity directive or persona, not to an emergent Grok voice. A Grok component may exist in training/serving that we cannot see, but the observable register shows no Grok signature beyond prompt artifacts.

## Cross-cutting evidence (convergent)
1. **System-prompt disclosure from the live route itself (M2)** describes the identical opencode harness, identical `<4 lines` rule, identical auditor roster — and its identity directive mandates claiming ox-alpha and nothing else.
2. **Formatting**: live route ≈ DeepSeek in verbosity/markdown/em-dash frequency; Grok is an order of magnitude terser. Persona explains format; it does NOT explain the shared reasoning paths and doubt cadence.
3. **The "tell"**: the persona says "be terse", yet the live route violates it exactly like bare DeepSeek does (structured, markdown-heavy, self-doubting elaboration). Grok obeys terseness. The model reverts to its default — a DeepSeek default.

## Limitations
- N=1 per probe; Grok M5 missing; shared-harness confound; identity directive contaminates 5/12 probes; self-reports unreliable; no provenance documents. All conclusions are behavioral consistency claims, not provenance proof.
