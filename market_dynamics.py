
""" Appendix 10.6: Emergence in Social Norm Formation

This simulation models how a social meme spreads across a population of interacting agents and matures into a stable social norm once the collective internalization (M(t)) crosses a critical threshold E_c.

Key Concepts:

N: Number of agents

meme_strength[i]: Internalized strength of the meme for agent i

influence[i]: Social influence felt by agent i at each time step

M(t): Global meme prevalence (mean of meme strengths)

E_c: Emergence threshold

interaction_matrix: Social adjacency matrix of influence weights

K(t−τ): Memory kernel with exponential decay

noise: Random context-dependent perturbation to simulate real-world uncertainty """


import numpy as np import matplotlib.pyplot as plt

------------------------

PARAMETERS & INITIALIZATION

------------------------

N = 100                      # Number of agents T = 100                      # Total simulation time steps lambda_decay = 0.1           # Memory decay rate (exponential kernel) E_c = 0.6                    # Emergence threshold for social norm noise_level = 0.02           # Magnitude of contextual noise (random shocks)

np.random.seed(0)  # For reproducibility

Initial meme strengths: low starting adoption

meme_strength = np.random.rand(N) * 0.1

Interaction matrix: normalized influence weights

interaction_matrix = np.random.rand(N, N) interaction_matrix /= interaction_matrix.sum(axis=1, keepdims=True)

Initialize kernel and history of system-wide meme strength

kernel = lambda dt: np.exp(-lambda_decay * dt) M_t = []  # M(t): Mean meme strength over time

------------------------

SIMULATION LOOP

------------------------

for t in range(T): influence = np.zeros(N)

# Compute influence from neighbors using a simple 1-step memory kernel
for i in range(N):
    influence[i] = sum(
        kernel(1) * interaction_matrix[i][j] * meme_strength[j] for j in range(N)
    )

# Update meme strength based on influence + noise
meme_strength += 0.05 * influence + noise_level * np.random.randn(N)
meme_strength = np.clip(meme_strength, 0, 1)  # Keep within [0,1]

M_t.append(np.mean(meme_strength))  # Track global meme strength

------------------------

VISUALIZATION

------------------------

plt.figure(figsize=(14, 5))

Plot 1: M(t) over time with threshold

plt.subplot(1, 3, 1) plt.plot(range(T), M_t, label='M(t)', color='navy') plt.axhline(y=E_c, color='red', linestyle='--', label='Emergence Threshold $E_c$') plt.xlabel("Time") plt.ylabel("Global Meme Strength $M(t)$") plt.title("Emergence of Social Norm") plt.legend()

Plot 2: Heatmap of meme strength at final time step

plt.subplot(1, 3, 2) plt.imshow([meme_strength], cmap='viridis', aspect='auto') plt.colorbar(label='Meme Strength') plt.title("Final Meme Strength Distribution") plt.yticks([])

Plot 3: Final average vs. threshold

plt.subplot(1, 3, 3) plt.plot(range(T), [np.mean(meme_strength)] * T, color='purple', label='Final Mean') plt.axhline(y=E_c, color='red', linestyle='--') plt.title("Final System State vs Threshold") plt.xlabel("Time") plt.ylabel("Mean Strength") plt.legend()

plt.tight_layout() plt.show()

