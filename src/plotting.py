import matplotlib.pyplot as plt

def plot_fidelity(fidelity_data, compression_thresholds):
    plt.figure(figsize=(10, 6))
    plt.plot(compression_thresholds, fidelity_data, marker='o', linestyle='-', color='b')
    plt.title('Fidelity of Hard Commitments vs. Compression Thresholds')
    plt.xlabel('Compression Threshold')
    plt.ylabel('Fidelity (Jaccard Index)')
    plt.grid()
    plt.xticks(compression_thresholds)
    plt.ylim(0, 1)
    plt.axhline(y=0.5, color='r', linestyle='--', label='Threshold for Identity Preservation')
    plt.legend()
    plt.tight_layout()
    plt.show()

def save_plot(fidelity_data, compression_thresholds, filename='fidelity_plot.png'):
    plt.figure(figsize=(10, 6))
    plt.plot(compression_thresholds, fidelity_data, marker='o', linestyle='-', color='b')
    plt.title('Fidelity of Hard Commitments vs. Compression Thresholds')
    plt.xlabel('Compression Threshold')
    plt.ylabel('Fidelity (Jaccard Index)')
    plt.grid()
    plt.xticks(compression_thresholds)
    plt.ylim(0, 1)
    plt.axhline(y=0.5, color='r', linestyle='--', label='Threshold for Identity Preservation')
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)

def plot_fid(sig_label, sigma_vals, fid_vals, outpath=None):
    plt.figure(figsize=(6,3))
    plt.plot(sigma_vals, fid_vals, marker='o')
    plt.xlabel("max_length (σ)")
    plt.ylabel("Fid_hard(σ)")
    plt.title(f"Fidelity vs σ — {sig_label}")
    plt.gca().invert_xaxis()
    plt.grid(True)
    if outpath:
        plt.savefig(outpath, bbox_inches='tight')
    else:
        plt.show()

def plot_delta(sig_label, steps, delta_vals, outpath=None):
    plt.figure(figsize=(6,3))
    plt.plot(steps, delta_vals, marker='o')
    plt.xlabel("recursion step n")
    plt.ylabel("Δ_hard(n)")
    plt.title(f"Drift vs n — {sig_label}")
    plt.grid(True)
    if outpath:
        plt.savefig(outpath, bbox_inches='tight')
    else:
        plt.show()
    plt.close()