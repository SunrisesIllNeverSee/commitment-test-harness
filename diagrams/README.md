# Diagrams for Commitment Conservation Paper

This folder contains all figures and diagrams referenced in the paper.

## Source Files

**fig1_shannon_commitment_chain.tex** - TikZ source for Shannon communication chain with commitment kernel and recursive feedback loop
  - Illustrates the transformation-stable communication system
  - Shows compression gate, invariant structure, and recursive application
  - Compile with: `pdflatex fig1_shannon_commitment_chain.tex`

## Generated Plots

**Fidelity vs. Compression Plots (fid_plot_*.png)**
  - Shows Fid_hard(σ) vs. σ for compression sweep tests
  - Demonstrates sharp threshold collapse under compression
  - Referenced in Section 8 (Exploratory Tests) and Section 4.2 (Falsification Protocol)

**Drift vs. Recursion Plots (delta_plot_*.png)**
  - Shows Δ_hard(n) vs. n for recursive transformation chains
  - Demonstrates commitment drift over recursive cycles
  - Referenced in Section 8.4 (Recursive Drift) and Section 4.3 (Falsification Protocol)

## Usage in Paper

- **Figure 1:** Shannon commitment chain (Section 3 or Section 5)
- **Figure 2:** Fidelity vs. compression threshold (Section 8.3)
- **Figure 3:** Drift vs. recursion depth (Section 8.4)

## Compilation

For LaTeX figures:
```bash
cd diagrams
pdflatex fig1_shannon_commitment_chain.tex
# Converts to PDF, then optionally to PNG:
convert -density 300 fig1_shannon_commitment_chain.pdf -quality 90 fig1_shannon_commitment_chain.png
```
