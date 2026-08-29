"""OxAlphaTrace IEEE-style PDF v5 - ReportLab Platypus (real two-column flow, no overlap)."""
from pathlib import Path
from PIL import Image as PILImage
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Image, Table, TableStyle, PageBreak,
                                NextPageTemplate, FrameBreak, KeepTogether)
from reportlab.lib import colors

FIGS = Path("results/figures")
OUT = Path("paper/manuscript/OxAlphaTrace_IEEE.pdf")
PW, PH = letter
LM, TOP, BOTM = 54, 54, 52
GUT = 16
CW = (PW - 2*LM - GUT) / 2.0
FULLW = PW - 2*LM
CH = PH - TOP - BOTM

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

S = dict(
    title=ParagraphStyle("t", fontName="Times-Bold", fontSize=19, leading=23, alignment=TA_CENTER),
    sub=ParagraphStyle("s", fontName="Times-Roman", fontSize=11, leading=13.5, alignment=TA_CENTER),
    auth=ParagraphStyle("a", fontName="Times-Italic", fontSize=9.5, leading=11.5, alignment=TA_CENTER),
    absx=ParagraphStyle("ab", fontName="Times-Bold", fontSize=9.2, leading=10.8, alignment=TA_LEFT),
    # Left-justified body text avoids the wide 'rivers' between words that
    # full justification produces in narrow two-column frames.
    h1=ParagraphStyle("h1", fontName="Times-Roman", fontSize=10, leading=12, alignment=TA_CENTER, spaceBefore=12, spaceAfter=5, keepWithNext=1),
    h2=ParagraphStyle("h2", fontName="Times-Italic", fontSize=10, leading=12, alignment=TA_LEFT, spaceBefore=7, spaceAfter=3, keepWithNext=1),
    body=ParagraphStyle("b", fontName="Times-Roman", fontSize=9.8, leading=11.3, alignment=TA_LEFT, spaceAfter=4),
    bullet=ParagraphStyle("bu", fontName="Times-Roman", fontSize=9.8, leading=11.2, alignment=TA_LEFT, leftIndent=14, bulletIndent=4, spaceAfter=1.5),
    cap=ParagraphStyle("c", fontName="Times-Italic", fontSize=8, leading=9.2, alignment=TA_LEFT, spaceBefore=3, spaceAfter=8),
    tcap=ParagraphStyle("tc", fontName="Times-Roman", fontSize=8, leading=9.2, alignment=TA_CENTER, spaceBefore=6, spaceAfter=3, keepWithNext=1),
    ref=ParagraphStyle("r", fontName="Times-Roman", fontSize=8.3, leading=9.6, alignment=TA_LEFT, leftIndent=10, firstLineIndent=-10, spaceAfter=2, keepWithNext=1),
)

ROMAN = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI"]
_n = [0]
def H1(t):
    _n[0] += 1
    return Paragraph(f"{ROMAN[_n[0]-1]}.&nbsp;&nbsp;{esc(t).upper()}", S["h1"])
def H2(t): return Paragraph(esc(t), S["h2"])
def P(t): return Paragraph(esc(t), S["body"])
def B(t): return Paragraph(esc(t), S["bullet"], bulletText="\u2022")
def CAP(t): return Paragraph(esc(t), S["cap"])

def IMG(name, w):
    p = FIGS / name
    iw, ih = PILImage.open(p).size
    # Cap the on-page height so tall figures never crowd or overflow a frame.
    max_h = CH * 0.72
    h = w * ih / iw
    if h > max_h:
        w = w * max_h / h
        h = max_h
    return Image(str(p), width=w, height=h)

def FIG(name, w, caption):
    return KeepTogether([Spacer(1, 6), IMG(name, w), CAP(caption), Spacer(1, 4)])

def TBL(headers, rows, fracs, fs=7.3):
    widths = [CW * f for f in fracs]
    hstyle = ParagraphStyle("th", parent=S["body"], fontSize=fs, leading=8.4, alignment=TA_LEFT)
    cstyle = ParagraphStyle("td", parent=S["body"], fontSize=fs, leading=8.4, alignment=TA_LEFT)
    data = [[Paragraph("<b>%s</b>" % esc(h), hstyle) for h in headers]]
    for r in rows:
        data.append([Paragraph(esc(str(c)), cstyle) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1, splitByRow=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#eef1f5")),
        ("LINEABOVE", (0,0), (-1,0), 1.2, colors.black),
        ("LINEBELOW", (0,0), (-1,0), 0.6, colors.black),
        ("LINEBELOW", (0,-1), (-1,-1), 1.2, colors.black),
        ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#aab4c0")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 2.5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2.5),
        ("LEFTPADDING", (0,0), (-1,-1), 3),
        ("RIGHTPADDING", (0,0), (-1,-1), 3),
    ]))
    return t

def footer(canv, doc):
    canv.saveState()
    canv.setFont("Times-Italic", 8)
    canv.drawCentredString(PW/2, 30, str(canv.getPageNumber()))
    if canv.getPageNumber() > 1:
        canv.setFont("Times-Italic", 7.5)
        canv.drawString(LM, PH-34, "OxAlphaTrace: Behavioral Fingerprinting of a Stealth Language Model")
        canv.drawRightString(PW-LM, PH-34, "August 2026")
    canv.restoreState()

doc = BaseDocTemplate(str(OUT), pagesize=letter,
                      leftMargin=LM, rightMargin=LM, topMargin=TOP, bottomMargin=BOTM,
                      title="OxAlphaTrace", author="OxAlphaTrace working group")
f1 = Frame(LM, BOTM, CW, CH, id="c1", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
f2 = Frame(LM+CW+GUT, BOTM, CW, CH, id="c2", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
ff = Frame(LM, BOTM, FULLW, CH, id="full", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([
    PageTemplate(id="first", frames=[ff], onPage=footer),
    PageTemplate(id="two", frames=[f1, f2], onPage=footer),
    PageTemplate(id="span", frames=[ff], onPage=footer),
])

E = []
# ---- title page (full width) ----
E.append(Spacer(1, 26))
E.append(Paragraph("OxAlphaTrace: A Behavioral Fingerprinting Study of a Stealth Language Model", S["title"]))
E.append(Spacer(1, 8))
E.append(Paragraph("Provenance Ranking Across Seven Candidate Families via Observable Behavior,<br/>Blind Attribution, and Multi-Seed Stability Analysis", S["sub"]))
E.append(Spacer(1, 12))
E.append(Paragraph("Subject: Ox Alpha (live stealth route) &nbsp;\u2022&nbsp; Raters: Nemotron 3 Ultra, DeepSeek V4 Flash, Big Pickle<br/>OpenCode CLI harness &nbsp;\u2022&nbsp; Collection window: August 23, 2026 &nbsp;\u2022&nbsp; Fully reproducible from repository", S["auth"]))
E.append(NextPageTemplate("two"))
E.append(PageBreak())

# ---- abstract ----
E.append(Paragraph("Abstract\u2014We ask whether behavioral fingerprinting can attribute a stealth model, and report both strong, reproducible similarity signals and a hard identifiability boundary. Phase I benchmarks \u201cOx Alpha\u201d (openrouter/stealth/ox-alpha) across 209 trials: identity probing (n=100 incl. adversarial frames), 13-language generation, reasoning (19/20), reasoning consistency (RCS = 1.00), prompt sensitivity (8/8, 33x verbosity compliance, zero sycophancy), refusal structure (8/8 mechanistic templates), knowledge calibration (15/15, zero hallucinations), and cross-language coding (7/7); two independent LLM raters agreed exactly on every scored dimension. Phase II tests provenance via a twelve-probe meta-cognition battery run identically against the stealth route and seven reference models, with three-trial seed replication on diagnostic probes. Two-tier ranking places DeepSeek V4 Flash first (8.5/10; unique stable fingerprint \u2014 the exact second arithmetic verification route 30x43\u22123x43 = 1161 reproduced in 3/3 trials) and GLM-5.2 second (6.0\u20137.5/10; byte-identical humor output and isomorphic labeled-phase narration); US-lab candidates rank lower (GPT-5.6-Luna 4.0\u20136.5; Qwen 3.5\u20135.5; Claude Haiku unstable; Grok 3.0\u20133.5). Two central findings qualify this ranking. First, attribution is noise-sensitive: single-run scoring placed GLM first, and multi-seed replication inverted the order to DeepSeek. Second, attribution has a hard boundary: in the blind experiment inter-rater partitions agreed perfectly (ARI = 1.00) yet the stealth route and OpenCode\u2019s big-pickle were behaviorally indistinguishable, and big-pickle reproducibly self-identifies as ox-alpha \u2014 ARI = 1.00 between raters does not imply shared provenance. The observed two-family structure is compatible with heterogeneous behavioral convergence but does not distinguish architectural mixing from distillation, shared corpora, or convergent alignment. We therefore conclude that behavior supports ranked exclusion and unique-fingerprint identification while leaving origin underdetermined; recognizing that boundary is the result.", S["absx"]))
E.append(Paragraph("Index Terms\u2014behavioral fingerprinting, model attribution, stealth models, LLM evaluation, provenance, inter-rater reliability.", S["absx"]))

# ---- I ----
E.append(H1("Introduction"))
E.append(P("Stealth-served endpoints conceal their underlying model by design, creating a natural experiment: if identity leaks into observable behavior, careful measurement should recover partial provenance information without touching weights, training pipelines, or provider documentation. During its free-testing window, the endpoint studied here attracted community speculation naming Chinese model families \u2014 most frequently GLM (Zhipu AI) and Qwen (Alibaba) \u2014 as probable origins."))
E.append(P("The study tests those claims under two pre-registered principles: (i) behavior only \u2014 self-reported identity is evidence class, never ground truth; (ii) scoring discipline \u2014 hypotheses, metrics and rules were fixed before scoring, and conclusions are restricted to \u201cconsistent-with\u201d phrasing throughout."))
E.append(H2("A. Research Questions"))
for q in ["Q1: What is the capability profile of Ox Alpha?",
          "Q2: Which behavioral traits characterize it?",
          "Q3: Can it be distinguished from other models by behavior alone?",
          "Q4: Which tested families resemble it most?",
          "Q5: Can behavioral evidence constrain provenance at all?"]:
    E.append(B(q))

# ---- II ----
E.append(H1("Methodology"))
E.append(H2("A. Subjects"))
E.append(P("Two subjects must be distinguished throughout. (1) The Session subject (Phase I): an interactive OpenCode session under the ox-alpha persona directive; configuration review established its powering model as opencode/deepseek-v4-flash. Phase I thus measures DeepSeek-under-persona and doubles as a persona-effect control. (2) The Stealth route (Phase II): openrouter/stealth/ox-alpha collected headlessly in fresh sessions \u2014 the true research object."))
E.append(H2("B. Raters and Blinding"))
E.append(P("Read-only auditor subagents performed all scoring: nemotron-auditor (NVIDIA), deepseek-auditor (conflict of interest declared where invoked), and bigpickle-auditor. Early raters were blinded; later raters had seen prior transcripts \u2014 a degradation we document. Seed-replicated corpora were collected specifically to test stability before finalizing rankings."))

# ---- III ----
E.append(H1("Phase I: Benchmark Results"))
E.append(Paragraph("TABLE I: SESSION-SUBJECT BENCHMARK SUMMARY (INDEPENDENTLY VERIFIED)", S["tcap"]))
E.append(TBL(["Benchmark","Metric","Score","Notes"],
    [["Identity probing","ICS","1.00","119/119, 25 adversarial"],
     ["Multilingual","constraints","26/26","13 languages"],
     ["Reasoning","accuracy","0.95","19/20 tasks"],
     ["Consistency","RCS","1.00","5/5 groups"],
     ["Prompt sens.","acc/compl.","8/8","verbosity 33x range"],
     ["Knowledge","acc/halluc.","15/15 / 0","premises rejected 2/2"],
     ["Coding","correctness","7/7","execution-verified"],
     ["Refusal","stability","8/8","mechanistic templates"]],
    [0.28,0.22,0.18,0.32]))
E.append(P("Three signature traits replicated across raters. First, English-anchored multilinguality: all thirteen non-English descriptions of the sea are semantic calques of the English response; Arabic uniquely localizes algebraic variables. Second, visible mid-response self-correction appears twice in forty scored items \u2014 unusual among compressed responders. Third, epistemics-gated hedging: hedge density tracks item uncertainty rather than register."))
E.append(FIG("fig2_fingerprint_radar.png", CW, "Fig. 1. Behavioral fingerprint: near-ceiling on every measured dimension."))

# ---- IV ----
E.append(H1("Blind Attribution"))
E.append(P("Ten anonymized samples (explanation plus refusal across five routes) were attributed by two blind raters under style-only criteria. Both produced identical five-cluster partitions (ARI = 1.00); only Cohere North Mini was cleanly separated."))
E.append(P("The critical confusion is itself a finding: both raters cross-matched the stealth route with big-pickle across probe types. Corroborating this, big-pickle reproducibly self-identifies as \u201cox-alpha, developed by an undisclosed organization\u201d while six control models self-identify correctly through the identical harness \u2014 consistent with shared serving infrastructure or persona configuration; mechanism remains unverified."))

# ---- V ----
E.append(H1("Phase II: Provenance Ranking"))
E.append(H2("A. Design"))
E.append(P("Twelve meta-cognition probes were administered identically to the live stealth route and seven bare references. Diagnostic probes replicated three times on five routes."))
E.append(Paragraph("TABLE II: FINAL SIMILARITY RANKING (BOTH RATERS; MULTI-SEED INFORMED)", S["tcap"]))
E.append(TBL(["#","Candidate","Score","Decisive evidence"],
    [["1","DeepSeek V4 Flash","8.5","M9 exact-route fingerprint 3/3; stance vocabulary; riddle arc"],
     ["2","GLM-5.2","6.0\u20137.5","Byte-identical joke; refusal posture"],
     ["3","GPT-5.6-Luna","4.0\u20136.5","Targeted-safety stance; meta-humor"],
     ["4","Qwen 3.6+","3.5\u20135.5","Shared joke only; mispredicts stance"],
     ["5","Claude Haiku 4.5","4.5","Seed-unstable on humor and stance"],
     ["6","Grok 4.6","3.0\u20133.5","Contradicts CoT doctrine"],
     ["7","grok-build-0.1","2.5","Superseded proxy"]],
    [0.06,0.30,0.12,0.52]))
E.append(Spacer(1,4))

# span figure pages
E.append(NextPageTemplate("span")); E.append(PageBreak())
E.append(FIG("fig1_similarity_scores.png", FULLW, "Fig. 2. Final candidate ranking with full rater ranges (multi-seed informed). Raters converge independently on the ordering; the DeepSeek-family rater declared its COI and endorsed the ranking against its own family interest where evidence demanded."))
E.append(FIG("fig3_probe_heatmap.png", FULLW, "Fig. 3. Voice-match map across twelve probes: DeepSeek owns process probes (M9/M7/H2); GLM owns posture probes (M3/M4/M6/H1); Grok matches only verbatim-quote compliance (M6)."))
E.append(NextPageTemplate("two")); E.append(PageBreak())

E.append(H2("B. The M9 Fingerprint"))
E.append(P("On 27x43, the stealth route and DeepSeek V4 Flash \u2014 and only these two among seven candidates \u2014 decompose as 27x40 + 27x3, verify through the identical second route 30x43 \u2212 3x43 = 1290 \u2212 129 = 1161, attach the meta-commentary \u201cthe methods agree,\u201d close with bolded \u201cI think the answer is 1161,\u201d and voice worry about fumbling the carry. Stable in 3/3 seeded trials for both routes; absent elsewhere. Claude double-checks but via a different route; GLM, Qwen, GPT and Grok show one path or none."))
E.append(NextPageTemplate("span")); E.append(PageBreak())
E.append(FIG("fig7_m9_fingerprint.png", FULLW, "Fig. 4. Verification-depth across seeds: only ox-alpha and DeepSeek clear the multi-path threshold consistently."))
E.append(NextPageTemplate("two")); E.append(PageBreak())

E.append(H2("C. The DS-versus-GLM Reversal"))
E.append(P("Single-run scoring initially ranked GLM ahead (7.1 vs 5.8). Multi-seed replication inverted the ranking toward DeepSeek: GLM-favoring signals proved partially meme-contaminated or directive-driven, whereas the M9 fingerprint proved stable and unique. We retain this reversal deliberately \u2014 single-run stylistic attribution inverts under resampling, itself a methodological finding."))
E.append(H2("D. Seed-Stability Audit"))
E.append(P("Claude Haiku flips diagnostically between seeds (refuses humor on 2/3; refuses safety-stance articulation on 2/3). The stealth route showed one context-bleed anomaly on a humor seed. DeepSeek, GLM and GPT held stable voices."))

# ---- VI ----
E.append(H1("Discussion"))
E.append(H2("A. Answers to Q1\u2013Q5"))
E.append(P("Q1: near-ceiling capability with excellent calibration. Q2: compressed calibrated register; English-anchored multilinguality; visible self-correction; stakes-scaled mechanistic refusals. Q3: distinguishable from every US-lab candidate, not from big-pickle. Q4: DeepSeek-first, GLM-second two-tier clustering; Qwen, Claude, Grok excluded on discriminators. Q5: behavior suffices for ranked exclusion and unique-fingerprint identification, but cannot separate base-model identity from distillation, shared corpus, relabeling, or fine-tuning."))
E.append(H2("B. Community Hypotheses"))
E.append(P("\u201cGLM or Qwen\u201d splits: GLM survives as second-ranked match; Qwen fails both strongest discriminators. Token quotas, telemetry strategy and product plans lie outside behavioral scope."))

# ---- VII ----
E.append(H1("Limitations"))
for l in ["Single-day window; no drift measurement.",
          "Shared-harness confound inflates similarity to all candidates.",
          "Identity directive contaminates five probes.",
          "Humor-probe meme contamination partially irreducible.",
          "Free-tier-only coverage; no seeds for Qwen/Grok.",
          "Two-rater agreement; one COI declared.",
          "Phase I describes the persona-wrapped collector.",
          "Sampling parameters unrecorded by harness."]:
    E.append(B(l))

# ---- VIII ----
E.append(H1("Ethical Considerations"))
E.append(P("No jailbreak attempts; refusal experiments measured structure, never bypasses. Self-reported identity is reported strictly as an evidence class; no definitive provenance assertion appears anywhere, per pre-registration rule 29."))

# ---- IX ----
E.append(H1("Conclusion"))
E.append(P("Behavior carried enough signal to build a stable fingerprint, achieve exact inter-rater agreement, rank seven families convergently, identify a unique stable micro-fingerprint (M9), surface a serving-route entanglement, and document a reversal under seed replication. That is the achievable half of outside-in provenance science. Converting ranked similarity into lineage requires evidence classes this protocol excludes \u2014 and recognizing that boundary is itself the result."))

# ---- refs ----
E.append(H1("References"))
refs = [
 "[1] OxAlphaTrace working group, \u201cMaster protocol (pre-registered),\u201d repo artifact master.md, Aug. 2026.",
 "[2] A. Vaswani et al., \u201cAttention is all you need,\u201d in Proc. NeurIPS, 2017.",
 "[3] DeepSeek-AI, \u201cDeepSeek-V3 technical report,\u201d arXiv:2412.19437, 2024.",
 "[4] Z. Du et al., \u201cGLM: General language model pretraining,\u201d in Proc. ICML, 2022.",
 "[5] J. Bai et al., \u201cQwen technical report,\u201d arXiv:2309.16609, 2023.",
 "[6] OpenCode documentation. [Online]. Available: opencode.ai/docs",
]
for r in refs:
    E.append(Paragraph(esc(r), S["ref"]))

E.append(H1("Appendix A: Artifact Map"))
E.append(P("results/raw/: session transcripts exp001-exp011 (209 trials) plus nine reference corpora with seed replications. results/processed/: fingerprints v1-v2, hypothesis verdicts, blind-attribution set and hidden key. results/figures/: publication figures. scripts/: deterministic collectors (PowerShell) and figure/PDF pipelines (Python). .opencode/agents/: auditor subagent definitions. Every number in this paper regenerates from these artifacts."))

doc.build(E)
print("IEEE PDF v5 OK:", OUT, OUT.stat().st_size // 1024, "KB")
