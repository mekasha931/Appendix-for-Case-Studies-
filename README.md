
Appendix: Simulations for Case Studies in Chapter 10

This appendix provides detailed simulations and computational models corresponding to each case study discussed in Chapter 10. Each simulation includes a description of key parameters and variables, explanation of visualized outputs, and clean Python code ready to run in a Jupyter Notebook or upload to GitHub.


---

10.2 Phase Transitions: Ferromagnetism to Paramagnetism

Description of Variables and Parameters

Lattice size (N): The number of spins along each dimension in the 2D Ising model.

Temperature (T): A critical control parameter influencing thermal fluctuations.

Spin configuration (S): A 2D matrix with elements +1 or -1 representing up or down spins.

Magnetization (M): The sum of all spins normalized by the total number of lattice points.

Emergence Threshold (E_c): Defined heuristically here as the temperature at which spontaneous magnetization disappears.


Simulation Output

The plot shows magnetization vs. temperature. The sharp drop around a critical temperature (T_c) represents a phase transition, marking the breakdown of collective order—an emergent phenomenon.

Python Code (Filename: ising_model_simulation.py)

import numpy as np
import matplotlib.pyplot as plt

# Initialize lattice
def initial_state(N):
    return np.random.choice([1, -1], size=(N, N))

def compute_energy(S):
    energy = 0
    N = S.shape[0]
    for i in range(N):
        for j in range(N):
            energy -= S[i, j] * (S[(i+1)%N, j] + S[i, (j+1)%N])
    return energy

def metropolis_step(S, T):
    N = S.shape[0]
    for _ in range(N**2):
        i, j = np.random.randint(0, N, 2)
        dE = 2 * S[i, j] * (S[(i+1)%N, j] + S[i, (j+1)%N] + S[(i-1)%N, j] + S[i, (j-1)%N])
        if dE < 0 or np.random.rand() < np.exp(-dE / T):
            S[i, j] *= -1
    return S

def simulate(N, temps, steps=5000):
    magnetizations = []
    for T in temps:
        S = initial_state(N)
        for _ in range(steps):
            S = metropolis_step(S, T)
        M = np.abs(np.sum(S)) / (N**2)
        magnetizations.append(M)
    return magnetizations

# Parameters
N = 50
temps = np.linspace(1.5, 3.5, 20)
magnetizations = simulate(N, temps)

# Plot
plt.plot(temps, magnetizations, marker='o')
plt.title("Phase Transition in 2D Ising Model")
plt.xlabel("Temperature (T)")
plt.ylabel("Magnetization (M)")
plt.grid(True)
plt.savefig("ising_phase_transition.png")
plt.show()

