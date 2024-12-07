import mixbox_3
from scipy.optimize import minimize
import numpy as np

def mixing_proportions(rgb1, rgb2, rgb3, target_rgb):
    z1 = mixbox_3.rgb_to_latent(rgb1)
    z2 = mixbox_3.rgb_to_latent(rgb2)
    z3 = mixbox_3.rgb_to_latent(rgb3)

    def objective(weights):
        w1, w2, w3 = weights
        z_mix = [w1 * z1[i] + w2 * z2[i] + w3 * z3[i] for i in range(mixbox_3.LATENT_SIZE)]
        mixed_rgb = mixbox_3.latent_to_rgb(z_mix)
        return np.sum((np.array(mixed_rgb) - np.array(target_rgb))**2)
    
    constraints = (
        {'type': 'eq', 'fun': lambda w: sum(w) - 1},
    )
    bounds = [(0, 1)] * 3

    initial_weights = [1/3, 1/3, 1/3]

    result = minimize(objective, initial_weights, constraints=constraints, bounds=bounds)
    return result.x if result.success else None

# Example colors (in RGB)
rgb1 = (252, 186, 3)    # Yellow
rgb2 = (210, 3, 252)    # Magenta
rgb3 = (32, 3, 252)    # Blue
target_rgb = (3, 211, 25)

proportions = mixing_proportions(rgb1, rgb2, rgb3, target_rgb)

print(f"Mixing proportions: {proportions}")
