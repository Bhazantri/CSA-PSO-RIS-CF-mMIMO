import numpy as np
import matplotlib.pyplot as plt
from pso import standard_pso
from csa_pso import csa_pso

def main():
    # Parameters
    D = 10  # Dimensions
    N = 20  # Particles
    T_max = 100  # Iterations
    bounds = (-np.pi, np.pi)  # Phase shift bounds

    # Set random seed for reproducibility
    np.random.seed(42)

    # Run algorithms
    gbest_pso, fitness_pso, history_pso = standard_pso(D, N, T_max, bounds)
    gbest_csa, fitness_csa, history_csa = csa_pso(D, N, T_max, bounds)

    # Print results
    print(f"Standard PSO - Best Fitness: {fitness_pso:.4f}, Best Solution: {gbest_pso[:5]}...")
    print(f"CSA-PSO - Best Fitness: {fitness_csa:.4f}, Best Solution: {gbest_csa[:5]}...")

    # Plot convergence
    plt.figure(figsize=(10, 6))
    plt.plot(history_pso, label='Standard PSO', color='blue')
    plt.plot(history_csa, label='CSA-PSO', color='red')
    plt.xlabel('Iteration')
    plt.ylabel('Best Fitness (Rastrigin)')
    plt.title('Convergence Comparison: Standard PSO vs CSA-PSO')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
