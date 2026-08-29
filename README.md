# OxAlphaTrace

**A Behavioral Fingerprinting Study of a Stealth Language Model**

Provenance ranking across seven candidate model families via observable behavior, blind attribution, and multi-seed stability analysis.

## What this is

OxAlphaTrace is an experimental, behavior-only research project investigating whether the **observable behavior** of a stealth-served language model — `openrouter/stealth/ox-alpha` — can function as a measurable fingerprint for model comparison, attribution, and provenance analysis.

The work deliberately treats self-reported identity as *evidence, never ground truth*, and restricts every conclusion to "consistent-with" phrasing (see the pre-registered protocol in [`master.md`](master.md)).

## Key results

- **Phase I (benchmarks):** near-ceiling capability profile — identity consistency 1.00 (119/119 incl. adversarial frames), reasoning 19/20, reasoning consistency RCS = 1.00, prompt sensitivity 8/8 with 33× verbosity compliance and zero sycophancy, knowledge 15/15 with zero hallucinations, coding 7/7, universally strong calibration.
- **Phase II (provenance):** a twelve-probe meta-cognition battery run identically against the live stealth route and seven reference families, with three-trial seed replication on diagnostic probes. Raters converge on a **two-tier ranking: DeepSeek V4 Flash first (8.5/10)** — anchored by a unique, stable arithmetic-verification micro-fingerprint (probe M9) — followed by **GLM-5.2 (Zhipu, 6.0–7.5/10)**. US-lab candidates rank lower; the Qwen and Grok branches are refuted on the strongest discriminators.
- **Blind attribution:** perfect inter-rater partition agreement (ARI = 1.00), but the stealth route and OpenCode's `big-pickle` were mutually indistinguishable and `big-pickle` reproducibly self-identifies as ox-alpha. No behavioral result establishes final lineage — that boundary is itself a finding.

## Repository layout

```
master.md                  Pre-registered research protocol & methodology
paper/
  manuscript/              Final paper (IEEE-style PDF, LaTeX, sources)
results/
  raw/                     Raw transcripts, reference corpora, seed replications
  processed/               Fingerprints, rater verdicts, attribution keys
  figures/                 Publication figures (Fig 1–7)
scripts/
  data_collection/         Reproducible collectors (PowerShell)
  visualization/           Figure + PDF rendering pipeline (Python)
.opencode/agents/          Auditor subagent definitions
```

## Reproducibility

Every number in the paper regenerates from artifacts in this repository:

- **Transcripts:** `results/raw/` (exp001–013, seven reference corpora, seed replications)
- **Verdicts & fingerprints:** `results/processed/`
- **Figures:** `scripts/visualization/make_figures*.py`
- **Paper PDF:** `scripts/visualization/render_ieee_pdf.py` (IEEE-style two-column layout)

## Ethical note

No jailbreak attempts were made; refusal experiments measured structure, never bypasses. No definitive provenance claim appears anywhere in this paper.

## License

MIT — see [LICENSE](LICENSE).
