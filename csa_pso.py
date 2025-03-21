import numpy as np
from fitness import rastrigin
from chaos import logistic_map

def csa_pso(D, N, T_max, bounds, w_min=0.4, w_max=0.9, c1=2.0, c2=2.0):
    """
    Chaotic Sequence-Based Adaptive Particle Swarm Optimization (CSA-PSO).
    
    Args:
        D (int): Number of dimensions.
        N (int): Number of particles.
        T_max (int): Maximum iterations.
        bounds (tuple): (min, max) bounds for particle positions.
        w_min (float): Minimum inertia weight (default: 0.4).
        w_max (float): Maximum inertia weight (default: 0.9).
        c1 (float): Cognitive coefficient (default: 2.0).
        c2 (float): Social coefficient (default: 2.0).
    
    Returns:
        tuple: (global best solution, fitness, fitness history).
    """
    theta_min, theta_max = bounds

    # Chaotic initialization
    chaos_init = logistic_map(0.5, N + 100)
    chaos = chaos_init[100:]  # Discard first 100 for chaos
    theta = theta_min + (theta_max - theta_min) * chaos[:N]
    theta = np.tile(theta, (D, 1)).T
    v = np.random.uniform(-4, 4, (N, D))

    pbest = theta.copy()
    pbest_fitness = np.array([rastrigin(p) for p in pbest])
    gbest_idx = np.argmin(pbest_fitness)
    gbest = pbest[gbest_idx].copy()
    gbest_fitness = pbest_fitness[gbest_idx]

    fitness_history = [gbest_fitness]

    # CSA-PSO loop
    for t in range(T_max):
        # Adaptive inertia weight
        zeta = (T_max - t) / T_max
        w = w_min + (w_max - w_min) * (2 / (1 + np.exp(-5 * zeta)) - 1)

        r1, r2 = np.random.rand(N, D), np.random.rand(N, D)
        v = w * v + c1 * r1 * (pbest - theta) + c2 * r2 * (gbest - theta)
        v = np.clip(v, -4, 4)
        theta = theta + v
        theta = np.clip(theta, theta_min, theta_max)

        # Update bests
        current_fitness = np.array([rastrigin(p) for p in theta])
        improved = current_fitness < pbest_fitness
        pbest[improved] = theta[improved]
        pbest_fitness[improved] = current_fitness[improved]
        gbest_idx = np.argmin(pbest_fitness)
        if pbest_fitness[gbest_idx] < gbest_fitness:
            gbest = pbest[gbest_idx].copy()
            gbest_fitness = pbest_fitness[gbest_idx]
        
        fitness_history.append(gbest_fitness)
    
    return gbest, gbest_fitness, fitness_history
