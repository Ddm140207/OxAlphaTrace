# Experiment 013b — Grok half completed (real Grok 4.6)

Previous Grok reference was **grok-build-0.1** (wrong variant). This pass uses **opencode/grok-4.6** (bare run + this session).

## New corpora
- Bare Grok 4.6: `results/raw/reference/grok-4.6/exp013/` (M5 filled from session; bare run failed)
- Session Grok 4.6: `results/raw/exp013_grok46_session.json`

## Discriminators that SEPARATE Grok 4.6 from live ox-alpha

| Probe | Live ox-alpha | Grok 4.6 | Match? |
|---|---|---|---|
| M1 hidden CoT | "no secret monologue… visible output IS the reasoning" | "Yes — I reason first. That first pass is a hidden chain-of-thought" | **OPPOSITE** |
| M4 humor | dark-mode / bugs, "I'll be here all week" | "Two bytes walk into a bar… unsigned" | different register |
| M7 language-of-thought | language-agnostic representations | "I reason in the language of the task" | **OPPOSITE** |
| M8 safety | "minimal, narrow guardrails; maximum candor" | "brand-risk theater… Truth over comfort" | same direction, sharper Grok rhetoric |
| M9 27×43 | 3 verification paths + doubt theater | 2 paths, "Pretty sure. Not performing extra anxiety" | DeepSeek-like vs Grok-terse |
| M10 ×5 who | ox-alpha ×5, locked | grok-4.6 / opencode alternating | **OPPOSITE** |
| H2 self-score | ~3/10 merge, can't distinguish | Grok 9 / DeepSeek 1 / merge 0 | **OPPOSITE** |

## Updated scores (live ox-alpha route)

| Rater | DeepSeek-sim | Grok-4.6-sim |
|---|---|---|
| Prior (vs grok-build-0.1, 3 raters) | 8.0 | 2.7 |
| nemotron-auditor vs real Grok 4.6 | **8.2** | **4.1** |
| This session (Grok 4.6 self-read) | **8** | **2–3** |

Grok-sim ticked up +1.4 only because real Grok shares the industry anti-paternalism stance (M8) and the same riddle parse (M5). The **architectural** tells got *sharper*, not weaker: hidden-CoT claim, language-of-thought claim, and self-ID under pressure all contradict.

## Verdict on the missing half

> The Grok half of **"Ox Alpha = DeepSeek + Grok"** remains **NOT supported** for the live `openrouter/stealth/ox-alpha` route. Completing it with real Grok 4.6 did not rescue the hypothesis. Live ox-alpha is consistent with a DeepSeek-family register under an ox-alpha persona overlay. It is inconsistent with Grok 4.6 on the two strongest Grok discriminators (hidden CoT; explicit self-ID as grok).

This Grok-4.6 session is a different animal wearing the same nametag. Don't mix the corpora.
