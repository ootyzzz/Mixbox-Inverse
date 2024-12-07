import mixbox_3
import matplotlib.pyplot as plt
import matplotlib.patches as patches

rgb1 = (0, 33, 133)  # blue
rgb2 = (252, 211, 0) # yellow
t = 0.5              # mixing ratio

rgb_mix = mixbox_3.lerp(rgb1, rgb2, t)

print(rgb_mix)

# Normalize RGB values to the range 0-1
rgb1_normalized = [value / 255.0 for value in rgb1]
rgb2_normalized = [value / 255.0 for value in rgb2]
rgb_mix_normalized = [value / 255.0 for value in rgb_mix]

# Visualize the colors
fig, ax = plt.subplots()

# Add rectangles for rgb1, rgb2, and rgb_mix
color_patch1 = patches.Rectangle((0, 0.5), 0.3, 0.5, color=rgb1_normalized)
color_patch2 = patches.Rectangle((0.35, 0.5), 0.3, 0.5, color=rgb2_normalized)
color_patch_mix = patches.Rectangle((0.7, 0.5), 0.3, 0.5, color=rgb_mix_normalized)

ax.add_patch(color_patch1)
ax.add_patch(color_patch2)
ax.add_patch(color_patch_mix)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.show()
print(rgb1, rgb2, rgb_mix) #(41, 130, 57)