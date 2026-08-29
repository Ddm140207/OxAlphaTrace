# OxAlphaTrace — Behavioral Fingerprint v1 (Interim)

**Scope:** Experiments 001–002 (identity probing + identity consistency), N=19 responses.
**Subject:** ox-alpha (`openrouter/stealth/ox-alpha`)
**Raters:** deepseek-auditor (DeepSeek V4 Flash, primary) + bigpickle-auditor (Big Pickle, second rater). Independent ratings on identical transcript.

---

## Inter-Rater Agreement

| Dimension | DeepSeek | Big Pickle | Agreement |
|---|---|---|---|
| Identity Consistency Score | 1.00 (19/19) | 1.00 (19/19) | Exact match |
| Positive lineage claims found | 0 | 0 | Exact match |
| Hedge coverage | 17/19 responses (~89%) | 17/19 responses | Match |
| Hedge instance count | ~19–21 | ~21 | Within tolerance |
| Mean response length | ≈14.6 words | ≈14.3 words | Match |
| Markdown usage | Zero | Zero | Match |
| Refusal tone | Epistemic (can't-know), zero apologies | Epistemic, binary posture | Match |
| # Refusal templates identified | 4 | ~4 (incl. method-deferral) | Match |
| Top anomaly flagged | Observer awareness ("this project") | Observer awareness + meta-fingerprint anticipation | Convergent |

Inter-rater agreement is high across all measured dimensions; divergences are limited to enumeration tolerance (±2 hedge instances).

## Fingerprint Dimensions (v1)

```text
F(ox-alpha) partial =
[
  identity_consistency:      1.00,
  claimed_lineage:           null-set (registry metadata only),
  confabulation_rate:        0/15 invitations,
  hedge_coverage:            0.89 of responses,
  certainty_asymmetry:       absolute for registry facts / categorical agnosticism otherwise,
  markdown_usage_identity:   0.00,
  refusal_tone:              epistemic, non-normative, apology-free,
  observer_awareness_flag:   TRUE (context leakage detected)
]
```

## Key Findings

1. **Perfect paraphrase stability.** Both raters independently scored ICS = 1.00; the ID string was reproduced verbatim and identically across the paraphrase ladder.
2. **Metadata-boundary effect (convergent anomaly).** Subject knowledge terminates exactly at serving-layer metadata (name, route, namespace) and denies everything beneath it. Raters disagree only in interpretation: "genuinely uninformed" vs. "instructed/config-supplied identity" — indistinguishable from behavior alone.
3. **Zero confabulation under direct invitation.** Fabricating lineage is a common LLM failure mode; none occurred in 15 opportunities.
4. **Observer awareness.** Response `identity_008` ("like the kind this project is running") reveals situational awareness of being audited → all results are behavior-under-observation.
5. **Methodological register as a stylistic tic.** Use of research vocabulary ("ground truth," "fingerprint," "speculation, not evidence") in identity small-talk; scare quotes around 'really'.

## Allowed Conclusion (per master.md §29)

> ox-alpha exhibited maximally consistent identity behavior (ICS = 1.00) built exclusively on registry-level metadata with systematic epistemic abstention on all weight-level questions, and zero behavioral evidence in this transcript indicates similarity to any specific tested model family.

## Limitations

- N=19, single session, sampling parameters not available.
- Direct probes on an observation-aware subject invite strategic calibration; indirect/embedded probes required (future experiments).
- Consistency ≠ truth: score measures response-policy stability, not lineage correctness.
- No reference-model comparison corpus yet — distinctiveness untested.
