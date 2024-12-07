import mixbox_3

# 生成100个等距测试点
test_points = [(i, j, k) for i in range(0, 256, 3) for j in range(0, 256, 3) for k in range(0, 256, 3)]

for color_rgb in test_points:
    # 将 RGB 颜色转换为 latent 表示
    latent = mixbox_3.rgb_to_latent(color_rgb)
    
    # 将 latent 表示转换回 RGB 颜色
    color_rgb_back = mixbox_3.latent_to_rgb(latent)
    
    # 检查转换前后的 RGB 是否相同
    if color_rgb != color_rgb_back:
        print(f"Difference found at Original RGB: {color_rgb}, Converted back to RGB: {color_rgb_back}")