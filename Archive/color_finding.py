import numpy as np

def calculate_color_mixing_weights(c1, c2, c3, ct):
    # Normalize the colors to [0, 1] for calculations
    color = np.array([c1, c2, c3], dtype=float) / 255.0
    target = np.array(ct, dtype=float) / 255.0

    # Solve for weights using least squares
    w, _, _, _ = np.linalg.lstsq(color.T, target, rcond=None)

    # Clip weights to ensure they remain in [0, 1]
    w = np.clip(w, 0, 1)

    # Calculate the resulting color
    rc = np.dot(w, color) * 255
    rc = np.clip(rc, 0, 255).astype(int)

    return w, tuple(rc)

print("Enter RGB values for the three arbitrary color and the target color.")
color1 = tuple(map(int, input("Color 1 (R G B): ").split()))
color2 = tuple(map(int, input("Color 2 (R G B): ").split()))
color3 = tuple(map(int, input("Color 3 (R G B): ").split()))
target_color = tuple(map(int, input("Target Color (R G B): ").split()))

weights, recreated_color = calculate_color_mixing_weights(color1, color2, color3, target_color)

print(f"\nTo approximate the target color {target_color}, use the following weights:")
print(f"Color 1: {weights[0]:.2f}")
print(f"Color 2: {weights[1]:.2f}")
print(f"Color 3: {weights[2]:.2f}")

print(f"\nThe recreated color is approximately: {recreated_color}")

# input (0, 33, 133) (252, 211, 0) (any random color, wont be used) (41, 130, 57)
# expect 0.5, 0.5, 0,
# gives: 
# To approximate the target color (41, 130, 57), use the following weights:
# Color 1: 0.96
# Color 2: 0.47
# Color 3: 0.00