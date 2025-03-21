import numpy as np

def logistic_map(x0, iterations):
    """
    Generate a chaotic sequence using the Logistic map.
    
    Args:
        x0 (float): Initial value (between 0 and 1).
        iterations (int): Number of iterations.
    
    Returns:
        np.ndarray: Chaotic sequence of length `iterations`.
    """
    chaos = [x0]
    for _ in range(iterations - 1):
        x = 4 * chaos[-1] * (1 - chaos[-1])  # Logistic map equation
        chaos.append(x)
    return np.array(chaos)
