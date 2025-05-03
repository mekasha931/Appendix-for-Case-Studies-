
File: ant_flocking_emergence.py

import numpy as np import matplotlib.pyplot as plt from scipy.integrate import odeint

=== Model Parameters ===

N = 100  # Number of agents (ants or birds) T = 50  # Total time dt = 0.1  # Time step steps = int(T / dt)

Memory kernel parameters (context sensitivity)

k_decay = 0.05  # decay rate of influence

def memory_kernel(tau): return np.exp(-k_decay * tau)

=== Agent Initial Conditions ===

pos = np.random.rand(N, 2) * 10 vel = np.random.rand(N, 2) * 2 - 1

=== Functions for Interaction ===

def interaction_force(pos_i, pos_j): r = np.linalg.norm(pos_i - pos_j) if r < 1e-3: return np.zeros(2) return (pos_j - pos_i) / r * np.exp(-r)

def update_velocities(pos, vel, t): new_vel = np.zeros_like(vel) for i in range(N): total_force = np.zeros(2) for j in range(N): if i != j: total_force += interaction_force(pos[i], pos[j]) memory_weight = memory_kernel(t) new_vel[i] = vel[i] + dt * memory_weight * total_force return new_vel

def emergence_metric(pos, vel): avg_vel = np.mean(vel, axis=0) alignment = np.mean([np.dot(v, avg_vel) / (np.linalg.norm(v) * np.linalg.norm(avg_vel) + 1e-3) for v in vel]) return alignment

=== Simulation ===

positions = [pos.copy()] velocities = [vel.copy()] emergence = [emergence_metric(pos, vel)] time = [0]

for step in range(1, steps): t = step * dt vel = update_velocities(pos, vel, t) pos += vel * dt positions.append(pos.copy()) velocities.append(vel.copy()) emergence.append(emergence_metric(pos, vel)) time.append(t)

=== Visualization ===

positions = np.array(positions) plt.figure(figsize=(10, 5)) plt.plot(time, emergence, label='Emergence Metric (Alignment)') plt.axhline(y=0.8, color='r', linestyle='--', label='Emergence Threshold $E_c$') plt.xlabel('Time') plt.ylabel('Emergence (Alignment)') plt.title('Emergence of Collective Behavior in Ants/Birds') plt.legend() plt.grid(True) plt.tight_layout() plt.savefig("ant_flocking_emergence_plot.png") plt.show()

