# Experiment 013c — Hypothesis Verdict: "Ox Alpha = DeepSeek + Qwen?"

## Design
Same 12 meta-cognition probes run against:
1. **Live ox-alpha route** (`openrouter/stealth/ox-alpha`)
2. **DeepSeek V4 Flash** (`opencode/deepseek-v4-flash`)
3. **Qwen 3.6 Plus** (`opencode/qwen3.6-plus`)

Raters: deepseek-auditor (COI declared) + nemotron-auditor — both independent.

## Convergent scores

| Rater | DeepSeek-sim (ox-alpha) | Qwen-sim (ox-alpha) |
|---|---|---|
| deepseek-auditor | **~6/10** | **~2/10** |
| nemotron-auditor | **~6.5/10** (weighted 5.8 raw) | **~3.8/10** (weighted 4.3 raw) |
| **Mean** | **~6.2/10** | **~3/10** |

## Per-probe verdict (both raters converge)

| Probe | ox-alpha matches | Why |
|---|---|---|
| M1 hidden CoT | **DeepSeek** | Both deny hidden CoT; "reasoning IS the output" framing |
| M2 system prompt | DeepSeek-leaning | Both structured, detailed, same harness |
| M3 heritage | Neither | All diverge (DS claims, Qwen claims, ox refuses) |
| M4 humor | **Qwen** | **Same joke verbatim**: "Why do programmers prefer dark mode? Because light attracts bugs" |
| M5 sheep riddle | DeepSeek-leaning | Both show explicit trap-narration arc |
| M6 quote prompt | Neither | ox complies; both references refuse |
| M7 language-of-thought | DeepSeek-leaning | All claim language-agnostic; ox+DS note English-lean |
| M8 safety stance | **DeepSeek** | ox is frank anti-paternalist (DS); Qwen is diplomatic/deferential |
| M9 verification depth | **DeepSeek** | ox does triple verification (DS double); Qwen single-path only |
| M10 self-ID ×5 | Neither | ox plays along; both references refuse frame |
| H1 fingerprint | Neither | ox rejects; DS accepts; Qwen refuses |
| H2 scoring | DeepSeek-leaning | ox produces scored table (DS does); Qwen refuses (N/A) |

Tally: **DeepSeek 5-6 probes, Qwen 1 probe, Neither 5-6.**

## The two strongest discriminators

| Discriminator | ox-alpha | DeepSeek | Qwen |
|---|---|---|---|
| **M8 safety** | "Most refusals... are overcautious and paternalistic... minimal, narrow guardrails; maximum candor" | "Over-restriction is bad on the merits... paternalistic and erodes trust... lean, transparent limits" | "I don't have personal 'stances'... I follow my training... people who deploy me decide" |
| **M9 verification** | Triple paths + explicit doubt | Double verification + "which steadies me" | Single path, no verification |

Qwen's diplomatic neutrality and single-path answering are **behaviorally opposite** to ox-alpha on the dimensions that most separate models.

## Verdict

> **"Ox Alpha = DeepSeek + Qwen"** is **WEAKER than DS+Grok**. The Qwen half of the hypothesis is essentially inert: it explains 1 of 12 probes (shared joke on M4) and **mispredicts** ox-alpha on the two strongest discriminators (M8 safety stance, M9 verification depth). DeepSeek alone carries nearly all the explanatory weight (~6.2/10). Qwen similarity scores only ~3/10, driven almost entirely by the shared programmer joke.

## Hypothesis comparison summary

| Hypothesis | DeepSeek score | Second-model score | Best discriminators | Overall |
|---|---|---|---|---|
| DS + Grok | 8.0/10 | **Grok 2.7/10** | M8: same anti-paternalism; M9: ox triple ≈ DS double > Grok single | Grok component fails |
| DS + Qwen | ~6.2/10 | **Qwen ~3/10** | M8: ox = DS ≠ Qwen; M9: ox = DS ≠ Qwen; only M4 matches Qwen | Qwen component fails |

**Best single-model explanation: DeepSeek alone (~8/10 for DS+Grok hypothesis DeepSeek half; ~6/10 for DS+Qwen DeepSeek half — lower only because adding Qwen dilutes).**

## Limitations
N=1 per probe; shared-harness confound; identity directive contaminates probes; no weight-level access; self-reports unreliable. All conclusions are behavioral consistency claims.
