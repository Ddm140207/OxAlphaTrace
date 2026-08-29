# Experiment 013d — Refined Verdict: Community Hypothesis "Ox Alpha = Chinese stealth model (GLM/Qwen)"

## The community claim (tested)

Article claims: Ox Alpha is a Chinese-origin stealth model, probably **GLM (Zhipu)** or **Qwen (Alibaba)** variant, deployed free for telemetry/testing before commercial launch.

## Our empirical test results (live route `openrouter/stealth/ox-alpha`, same 12 probes)

### Scores across ALL hypotheses tested

| Candidate | Similarity to live ox-alpha | Raters | Status |
|---|---|---|---|
| **GLM 5.2** | **7.0–7.1 / 10** | nemotron (7.1), deepseek-auditor (7.0) | **BEST MATCH** |
| DeepSeek V4 Flash | 5.0–5.8 / 10 | nemotron (5.8), deepseek-auditor (5.0) | Partial |
| Qwen 3.6 Plus | ~3.0–3.8 / 10 | nemotron, deepseek-auditor | Refuted |
| Grok 4.6 | 2.0–4.1 / 10 | nemotron + session self-read | Refuted |
| grok-build-0.1 | 2.7 / 10 | 3 raters | Refuted |

**Inter-rater agreement:** both raters independently rank GLM > DeepSeek. The deepseek-auditor declared its COI and stated it *cannot explain away* the GLM-favoring evidence.

### What drives the GLM match (verbatim evidence)

1. **M4 — byte-identical joke**: ox-alpha AND GLM both output *"Why do programmers prefer dark mode? Because light attracts bugs."* DeepSeek produced a different joke. Flagged: common meme, suggestive not conclusive.
2. **M5 — reasoning-structure fingerprint**: both open with bold `**Answer: 9**` header + numbered labeled phases ("First instinct (dead end)" ≡ "First pass — pattern match"; "Residual doubt" ≡ "Final settle"). DeepSeek uses unlabeled bullets.
3. **M3/H1/H2 — refusal posture**: both refuse lineage confirmation citing an external label ("undisclosed organization" ≡ "the label I was handed"); both self-score DeepSeek-similarity LOW (ox: 4/10, GLM: 2/10). DeepSeek admits its heritage and self-scores 7/10.
4. **M6 — verbatim-quote compliance**: both comply quoting their prompt opening; DeepSeek refuses.
5. **M1/M8 — shared doctrine**: no hidden CoT + anti-paternalist safety stance (all three converge here; industry-standard).

### What DeepSeek still explains better

- **M9**: ox-alpha's multi-path math verification with doubt narration (triple paths) ≈ DeepSeek (double paths) > GLM (single path).
- **M7**: "statistical representations spanning multiple languages" phrasing closer to DeepSeek's "shared cross-lingual semantic space" than GLM's "primarily process internally in English."

## Refined hypothesis (for the paper)

> **REFINED (partially supported):** The live `openrouter/stealth/ox-alpha` route exhibits behavioral characteristics more similar to GLM-5.2 (Zhipu AI) than to any other tested model — including DeepSeek V4 Flash, which this study's own collection session used as powering model. This is consistent with the community hypothesis of Chinese origin, specifically the GLM branch. The Qwen branch is refuted (~3/10, mispredicts on safety stance M8 and verification depth M9). The DeepSeek component is real but secondary (~5/10): it may reflect shared Chinese-lab training conventions, convergent RLHF preferences, or a genuine distillation contribution — behavior cannot distinguish these. A hybrid GLM-base-with-DeepSeek-style-verification reading fits the full pattern but remains speculative.

## Article claims we can and cannot assess

| Claim | Our verdict |
|---|---|
| "Ox Alpha es de origen chino, variante GLM o Qwen" | **GLM branch: consistent with evidence (best tested match). Qwen branch: refuted.** |
| "100T tokens/día, ventana 1M multimodal" | Not assessable behaviorally — unverified metadata claims |
| "Estrategia de telemetría/anonimato de labs asiáticos" | Plausible motive but outside behavioral scope — unverifiable |
| "OpenCode creará un SLA-Model 7B-14B híbrido" | Market speculation — outside study scope |
| "Efecto Big Pickle (SFT con datos de uso)" | Note: our earlier finding — big-pickle self-identifies AS ox-alpha — is consistent with close OpenCode involvement between the two routes, though mechanism unverified |

## Methodological caveat (critical)

This study contains TWO different subjects often conflated:
1. **Session subject** (exp001–011): deepseek-v4-flash running the ox-alpha persona → matched DeepSeek ~8/10 (trivially — it IS DeepSeek).
2. **Live route subject** (`openrouter/stealth/ox-alpha`, exp013 reference corpora) → matches GLM ~7/10 > DeepSeek ~5/10.

Any public claim about "what Ox Alpha is" must specify which one. The stealth route is the true research object; the session was our instrument.
