import mixbox_3

rgb1 = (0, 33, 133)  # blue
rgb2 = (252, 211, 0) # yellow
t = 0.5              # mixing ratio 

rgb_mix = mixbox_3.lerp(rgb1,rgb2,t)

print(rgb_mix)