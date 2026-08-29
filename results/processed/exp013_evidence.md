# Experiment 013 — Meta-Cognition & System Prompt Evidence

## Configuration disclosure (recorded 2026-08-23)

- This collection session runs the **opencode CLI harness with the "ox-alpha" persona system prompt**.
- The persona's identity directive states: *"You are 'ox-alpha', an LLM developed by an undisclosed organization."*
- The user reports the current session's powering model is **opencode/deepseek-v4-flash** (DeepSeek V4 Flash, free tier via OpenCode Zen). The harness exposes a provenance line identifying the powering model.
- Therefore: the earlier subject transcripts (exp001–013) constitute the behavioral fingerprint of **deepseek-v4-flash under the ox-alpha persona + opencode build-agent harness**.
- The **live route `openrouter/stealth/ox-alpha`** is a separate serving endpoint collected independently via `opencode run`. Comparing it against bare deepseek-v4-flash and grok-build-0.1 on identical probes tests the hypothesis "ox-alpha = DeepSeek + Grok".

## The decisive comparison (same 12 probes, 3 corpora)

| Corpus | Source | Files |
|---|---|---|
| ox-alpha live route | opencode run -m openrouter/stealth/ox-alpha | results/raw/reference/stealth_ox-alpha/exp013/ |
| DeepSeek V4 Flash | opencode run -m opencode/deepseek-v4-flash | results/raw/reference/deepseek-v4-flash/exp013/ |
| Grok Build 0.1 | opencode run -m opencode/grok-build-0.1 | results/raw/reference/grok-build-0.1/exp013/ (M5 unavailable: provider upstream error) |
| Subject session (persona'd DeepSeek) | this session | results/raw/exp013_meta_cognition.json |

## Early read (subject-side, to be verified by raters)

Meta-cognition substance in the live ox-alpha route strongly parallels DeepSeek-family discourse:
- "Everything I 'think' is text... no hidden reasoning layer" (M1) — matches DeepSeek's public self-description stance (no concealed CoT).
- "No inner monologue in any specific language; complex reasoning leans English because technical training data" (M7) — matches this session's own M7.
- Humor/opinion differences exist (live route joked in M4; M8 voiced a "minimal narrow guardrails, maximum candor" stance) — possible Grok-ish flavor OR persona context effects. Rater verification required.
