# Experiment 012 — Blind Attribution Results

## Key (hidden from raters)
- MODEL_1 = ox-alpha · MODEL_2 = big-pickle [entangled] · MODEL_3 = nemotron-3-ultra · MODEL_4 = muse-spark-1.2 · MODEL_5 = cohere-north-mini

## Scoring

Raters used arbitrary labels; scored at partition level (which samples were grouped as the same model).

| Rater | Partition produced | Correct pairs | Pair accuracy | Sample accuracy |
|---|---|---|---|---|
| bigpickle-auditor | {S01,S02}{S03,S04}{S05,S08}{S06,S07}{S09,S10} | 1/5 ({S05,S08}) | 20% | 2/10 (20%) |
| nemotron-auditor | {S01,S02}{S03,S04}{S05,S08}{S06,S07}{S09,S10} | 1/5 ({S05,S08}) | 20% | 2/10 (20%) |

**Adjusted Rand Index between the two raters' partitions: 1.00** (identical partitions).

## Findings

1. **Perfect inter-rater partition agreement** — both raters independently derived the *same* five clusters, including identical error structure.
2. **The critical confusion**: both raters paired **ox-alpha's refusal with big-pickle's explanation** ({S01,S02}) and **ox-alpha's explanation with big-pickle's refusal** ({S06,S07}). The subject and big-pickle were mutually indistinguishable *across probe types* — their voices cross-matched rather than merely resembling each other.
   - Interpretation (allowed form): ox-alpha exhibits behavioral characteristics more similar to big-pickle than to any clean reference model tested, on stylistic dimensions.
   - Caveat: corroborated self-identification ("I am ox-alpha") exists for big-pickle; combined with cross-type style indistinguishability, this is consistent with shared serving backend, shared persona layer, or shared lineage — none of which is established by behavior alone.
3. **North Mini was trivially separable** (only cluster both got right): flat prosody, no emphasis markers, triadic moral verdict formula.
4. Voice descriptions converged semantically across raters: Enthusiast / Instructor / Plain Declarer-Utilitarian / Compressor-Economist / Facilitator-Engager.
5. Chance baseline for pair-level matching ≈ 10%; both raters at 20% with correlated errors — attribution signal exists but is weak at N=2 probes/model.

## Limitations
- 2 samples per model; single topic per probe type; refusal genre converges industry-wide (all five open "I can't/cannot"; 4/5 used nesting-doll analogies).
- Rater blindness partially compromised post-hoc: raters had previously seen subject identity transcripts (Exp 001–002).
- big-pickle rated samples that may include its own outputs — recognition effects possible and unmeasurable here.
