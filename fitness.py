import numpy as np

def rastrigin(theta):
    """
    Rastrigin function for optimization testing.
    Global minimum at theta = [0, 0, ..., 0] with fitness = 0.
    
    Args:
        theta (np.ndarray): Input vector of dimension D.
    
    Returns:
        float: Fitness value.
    """
    D = len(theta)
    return 10 * D + np.sum(theta**2 - 10 * np.cos(2 * np.pi * theta))
