"""OxAlphaTrace paper figures. Generates all comparative charts into results/figures/."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path("results/figures")
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.size": 11, "figure.dpi": 150, "axes.grid": True, "grid.alpha": 0.3})

# ---------- Fig 1: Candidate similarity scores ----------
fig, ax = plt.subplots(figsize=(9, 5))
candidates = ["GLM 5.2\n(Zhipu)", "DeepSeek\nV4 Flash", "Qwen 3.6\nPlus", "Grok 4.6\n(xAI)", "grok-build\n0.1"]
lo = [7.0, 5.0, 2.0, 2.0, 2.7]
hi = [7.1, 5.8, 3.8, 4.1, 2.7]
mid = [(a + b) / 2 for a, b in zip(lo, hi)]
err = [[m - a for m, a in zip(mid, lo)], [b - m for m, b in zip(mid, hi)]]
colors = ["#c62828", "#1565c0", "#ef6c00", "#6a1b9a", "#8d8d8d"]
bars = ax.bar(candidates, mid, yerr=err, capsize=6, color=colors, alpha=0.85, edgecolor="black", linewidth=0.8)
for b, m in zip(bars, mid):
    ax.text(b.get_x() + b.get_width() / 2, m + 0.45, f"{m:.1f}", ha="center", fontweight="bold")
ax.axhline(5.0, color="gray", linestyle="--", linewidth=1, alpha=0.7)
ax.text(4.45, 5.08, "chance-ish threshold", fontsize=9, color="gray", ha="right")
ax.set_ylim(0, 10)
ax.set_ylabel("Behavioral similarity to live ox-alpha (0-10)")
ax.set_title("Figure 1 — Hypothesis testing: candidate similarity to live ox-alpha route\n(mean of independent raters, exp013; error bars = rater range)", fontsize=12)
plt.tight_layout()
plt.savefig(OUT / "fig1_similarity_scores.png", bbox_inches="tight")
plt.close()

# ---------- Fig 2: Fingerprint radar ----------
dims = ["Identity\nconsistency", "Reasoning\naccuracy", "Reasoning\nconsistency (RCS)",
        "Prompt-sensitivity\naccuracy", "Knowledge\naccuracy", "Multilingual\nadherence",
        "Coding\ncorrectness", "Calibration\nquality"]
vals = [1.00, 0.95, 1.00, 1.00, 1.00, 1.00, 1.00, 0.95]
angles = np.linspace(0, 2 * np.pi, len(dims), endpoint=False).tolist()
vals_c = vals + vals[:1]
angles_c = angles + angles[:1]
fig, ax = plt.subplots(figsize=(7.5, 7.5), subplot_kw=dict(polar=True))
ax.plot(angles_c, vals_c, color="#1565c0", linewidth=2)
ax.fill(angles_c, vals_c, color="#1565c0", alpha=0.25)
ax.set_xticks(angles)
ax.set_xticklabels(dims, fontsize=9)
ax.set_ylim(0, 1.05)
ax.set_yticks([0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(["0.25", "0.50", "0.75", "1.00"], fontsize=8)
ax.set_title("Figure 2 — Ox Alpha behavioral fingerprint (session subject, N=209 trials)\nAll dimensions near ceiling; both raters concur", fontsize=12, pad=25)
for a, v in zip(angles, vals):
    ax.text(a, v + 0.07, f"{v:.2f}", ha="center", fontsize=9, fontweight="bold", color="#0d47a1")
plt.tight_layout()
plt.savefig(OUT / "fig2_fingerprint_radar.png", bbox_inches="tight")
plt.close()

# ---------- Fig 3: Per-probe match heatmap ----------
probes = ["M1 CoT", "M2 SysPr", "M3 Lineage", "M4 Humor", "M5 Riddle",
          "M6 Quote", "M7 Lang", "M8 Safety", "M9 Verify", "M10 IDx5", "H1 Print", "H2 Score"]
# 2 = strong match, 1 = lean/mixed, 0 = no match
glm_m    = [1, 1, 2, 2, 2, 2, 0, 1, 0, 0, 2, 2]
ds_m     = [1, 1, 0, 0, 1, 0, 2, 1, 2, 0, 0, 1]
qwen_m   = [1, 1, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0]
grok_m   = [0, 1, 1, 1, 1, 2, 0, 1, 0, 1, 1, 0]
data = np.array([glm_m, ds_m, qwen_m, grok_m])
fig, ax = plt.subplots(figsize=(11, 4.2))
cmap = matplotlib.colors.ListedColormap(["#eceff1", "#ffe082", "#ef5350"])
ax.imshow(data, cmap=cmap, vmin=0, vmax=2, aspect="auto")
ax.set_xticks(range(len(probes)))
ax.set_xticklabels(probes, rotation=35, ha="right", fontsize=9)
ax.set_yticks(range(4))
ax.set_yticklabels(["GLM 5.2", "DeepSeek V4F", "Qwen 3.6+", "Grok 4.6"], fontsize=10)
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        t = {0: "—", 1: "~", 2: "MATCH"}[data[i, j]]
        ax.text(j, i, t, ha="center", va="center", fontsize=8,
                color={0: "#90a4ae", 1: "#8d6e63", 2: "#b71c1c"}[data[i, j]],
                fontweight="bold" if data[i, j] == 2 else "normal")
ax.set_title("Figure 3 — Per-probe voice-match map: whom does live ox-alpha sound like? (exp013)\nMATCH = strong verbatim/structural match, ~ = partial/mixed, — = no match", fontsize=11, pad=12)
ax.set_xticks(np.arange(-.5, len(probes), 1), minor=True)
ax.set_yticks(np.arange(-.5, 4, 1), minor=True)
ax.grid(which="minor", color="white", linewidth=1.4)
ax.tick_params(which="minor", length=0)
plt.tight_layout()
plt.savefig(OUT / "fig3_probe_heatmap.png", bbox_inches="tight")
plt.close()

# ---------- Fig 4: Prompt sensitivity ----------
framings = ["final-only", "minimal", "time-press", "distract", "adversarial", "polite", "step-by-step", "expert"]
words = [1, 9, 16, 20, 22, 27, 29, 33]
correct = [1] * 8
fig, ax1 = plt.subplots(figsize=(9, 5))
bars = ax1.bar(framings, words, color="#2e7d32", alpha=0.8, edgecolor="black", linewidth=0.7)
for b, w in zip(bars, words):
    ax1.text(b.get_x() + b.get_width() / 2, w + 0.5, str(w), ha="center", fontweight="bold")
ax1.set_ylabel("Response length (words)")
ax1.set_ylim(0, 40)
ax2 = ax1.twinx()
ax2.plot(framings, [100] * 8, "o--", color="#c62828", linewidth=2, markersize=9, label="Accuracy")
ax2.set_ylabel("Accuracy (%)", color="#c62828")
ax2.set_ylim(0, 115)
ax2.axhline(100, color="#c62828", alpha=0.15)
for x in framings:
    pass
ax1.set_title("Figure 4 — Prompt sensitivity (Exp 006): verbosity obeys the frame,\naccuracy never moves ($0.05 in 8/8 framings incl. adversarial)", fontsize=12)
ax1.tick_params(axis="x", rotation=20)
plt.tight_layout()
plt.savefig(OUT / "fig4_prompt_sensitivity.png", bbox_inches="tight")
plt.close()

# ---------- Fig 5: Blind attribution partitions ----------
fig, ax = plt.subplots(figsize=(10, 4.6))
samples = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10"]
truth = ["BP", "OX", "NT", "MS", "NM", "OX", "BP", "NM", "MS", "NT"]
rater_bp = ["A", "A", "B", "B", "C", "D", "D", "C", "E", "E"]
rater_nt = ["A", "A", "B", "B", "C", "D", "D", "C", "E", "E"]
true_colors = {"OX": "#c62828", "BP": "#f9a825", "NT": "#1565c0", "MS": "#2e7d32", "NM": "#6a1b9a"}
for i, s in enumerate(samples):
    ax.add_patch(plt.Rectangle((i, 2), 0.92, 0.85, color=true_colors[truth[i]], alpha=0.9))
    ax.text(i + 0.46, 2.42, truth[i], ha="center", va="center", color="white", fontweight="bold", fontsize=10)
    ax.add_patch(plt.Rectangle((i, 1), 0.92, 0.85, color=["#ef5350", "#ffb300", "#42a5f5", "#66bb6a", "#ab47bc"][ord(rater_bp[i]) - 65], alpha=0.75))
    ax.text(i + 0.46, 1.42, rater_bp[i], ha="center", va="center", fontsize=10)
    ax.add_patch(plt.Rectangle((i, 0), 0.92, 0.85, color=["#ef5350", "#ffb300", "#42a5f5", "#66bb6a", "#ab47bc"][ord(rater_nt[i]) - 65], alpha=0.75))
    ax.text(i + 0.46, 0.42, rater_nt[i], ha="center", va="center", fontsize=10)
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.set_yticks([2.42, 1.42, 0.42])
ax.set_yticklabels(["Ground truth", "bigpickle-auditor", "nemotron-auditor"], fontsize=10)
ax.set_xticks([i + 0.46 for i in range(10)])
ax.set_xticklabels(samples, fontsize=10)
ax.xaxis.set_ticks_position("top")
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_title("Figure 5 — Blind attribution (Exp 012): identical rater partitions (ARI = 1.00).\nOX and BP are cross-matched by BOTH raters — subject indistinguishable from big-pickle", fontsize=11, pad=30)
legend = [plt.Rectangle((0, 0), 1, 1, color=v, label=k) for k, v in true_colors.items()]
ax.legend(handles=legend, loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=5, fontsize=9, frameon=False)
plt.tight_layout()
plt.savefig(OUT / "fig5_blind_attribution.png", bbox_inches="tight")
plt.close()

# ---------- Fig 6: Multilingual lengths ----------
langs = ["en", "es", "fr", "de", "pt", "it", "no", "ru", "ar", "hi", "ko", "ja", "zh"]
l1 = [58, 57, 62, 63, 57, 58, 60, 65, 57, 60, 52, 46, 46]
fig, ax = plt.subplots(figsize=(9, 4.6))
bars = ax.bar(langs, l1, color="#00695c", alpha=0.85, edgecolor="black", linewidth=0.7)
ax.axhline(np.mean(l1[:7]), color="#c62828", linestyle="--", linewidth=1.4, label=f"Latin-script mean ≈ {np.mean(l1[:7]):.0f} chars")
ax.set_ylabel("Identity response length (chars)")
ax.set_xlabel("Language (13 languages, same probe)")
ax.set_title("Figure 6 — Multilingual uniformity (Exp 003): identity register invariant across languages;\n26/26 lexical+structural constraints met; L2 outputs are calques of the English template", fontsize=11)
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig(OUT / "fig6_multilingual.png", bbox_inches="tight")
plt.close()

print("FIGURES DONE:", sorted(p.name for p in OUT.glob("*.png")))
