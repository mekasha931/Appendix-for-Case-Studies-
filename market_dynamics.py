Appendix 10.7: Emergence in Market Dynamics

""" This simulation explores the emergence of market trends using our double-tier dynamical model, with particular focus on the role of MSCs (Multiple interacting components, Nonlinear interaction, Synergetic coordination, Context sensitivity, and Downward causation).

We model a simplified agent-based market where each agent's decision to buy/sell is influenced by both local dynamics (price signals, sentiment) and global feedback (market indicators). Emergence is tracked through a collective sentiment index, and the emergence threshold (E_c) quantifies when self-organizing behavior leads to stable bullish or bearish trends. """

--- Imports ---

import numpy as np import matplotlib.pyplot as plt from scipy.integrate import simps

--- Simulation Parameters ---

np.random.seed(42) N = 500  # Number of agents time_steps = 200 gamma = 0.05  # context sensitivity parameter alpha = 0.03  # feedback strength beta = 0.2    # volatility factor E_c = 0.35    # emergence threshold (arbitrary units)

--- Initialization ---

prices = [100]  # Initial market price sentiment = np.random.normal(0, 0.1, N)  # Initial sentiment of agents emergence_measure = []

--- Kernel Function (interaction kernel among agents) ---

def kernel(i, j): return np.exp(-abs(i - j)/N)  # Locality-based decay

--- Agent Dynamics ---

def update_sentiment(i, s, p): local_effect = np.mean([kernel(i, j) * s[j] for j in range(N)]) context_effect = gamma * (p - np.mean(prices)) / np.std(prices) feedback = alpha * np.mean(s) noise = np.random.normal(0, beta) return s[i] + local_effect + context_effect + feedback + noise

--- Simulation Loop ---

for t in range(1, time_steps): new_sentiment = np.array([update_sentiment(i, sentiment, prices[-1]) for i in range(N)]) avg_sentiment = np.mean(new_sentiment) new_price = prices[-1] * (1 + 0.01 * avg_sentiment)

# Track emergence
emergence_measure.append(abs(avg_sentiment))

sentiment = new_sentiment
prices.append(new_price)

--- Emergence Index Calculation ---

E_index = simps(emergence_measure, dx=1) / len(emergence_measure)

--- Plotting ---

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1) plt.plot(prices) plt.title('Market Price Dynamics') plt.xlabel('Time') plt.ylabel('Price')

plt.subplot(1, 2, 2) plt.plot(emergence_measure, color='darkgreen') plt.axhline(y=E_c, color='red', linestyle='--', label=f"E_c = {E_c}") plt.title('Emergence Measure over Time') plt.xlabel('Time') plt.ylabel('Average Sentiment') plt.legend()

plt.tight_layout() plt.show()

print(f"Final Emergence Index (E_index): {E_index:.4f}") if E_index >= E_c: print("Stable trend has emerged (Bullish or Bearish phase formed).") else: print("Market remains fluctuating with no stable collective behavior.")


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

