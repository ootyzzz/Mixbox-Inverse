import mixbox
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def find_target_color(rgb1, rgb2, rgb3, w1, w2, w3):

    # 转换 RGB 到 latent 空间
    z1 = mixbox.rgb_to_latent(rgb1)
    z2 = mixbox.rgb_to_latent(rgb2)
    z3 = mixbox.rgb_to_latent(rgb3)

    # 初始化混合 latent 向量
    z_mix = [0] * mixbox.LATENT_SIZE

    # 根据权重混合 latent 向量
    for i in range(len(z_mix)):
        z_mix[i] = w1 * z1[i] + w2 * z2[i] + w3 * z3[i]

    # 转换混合后的 latent 向量回到 RGB
    target_color = mixbox.latent_to_rgb(z_mix)
    return target_color

def find_2(rgb1, rgb2, w1, w2):
    # 转换 RGB 到 latent 空间
    z1 = mixbox.rgb_to_latent(rgb1)
    z2 = mixbox.rgb_to_latent(rgb2)

    # 初始化混合 latent 向量
    z_mix = [0] * mixbox.LATENT_SIZE

    # 根据权重混合 latent 向量
    for i in range(len(z_mix)):
        z_mix[i] = w1 * z1[i] + w2 * z2[i]

    # 转换混合后的 latent 向量回到 RGB
    target_color = mixbox.latent_to_rgb(z_mix)
    return target_color

def find_target_iter(rgb1, rgb2, rgb3, w1, w2, w3):
    # 递归混合颜色
    if w1 == 1:
        return rgb1
    elif w2 == 1:
        return rgb2
    elif w3 == 1:
        return rgb3
    else:
        mixed_color = find_2(rgb1, rgb2, w1, w2)
        return find_2(mixed_color, rgb3, (w1 + w2), w3)

def plot_colors_with_weights(ax, colors, titles, weights=None):
    for i, (color, title) in enumerate(zip(colors, titles)):
        ax[i].set_title(title)
        ax[i].add_patch(patches.Rectangle((0, 0), 1, 1, color=tuple(c / 255 for c in color)))
        if weights is not None and i < len(weights):  # 仅对前三个颜色显示权重
            ax[i].text(0.5, -0.1, f'w{i + 1} = {weights[i]:.2f}', ha='center', va='center', transform=ax[i].transAxes)
        ax[i].axis('off')

if __name__ == "__main__":
    rgb1 = (0, 33, 133)  # blue
    rgb2 = (252, 211, 0) # yellow
    rgb3 = (255, 0, 255) # magenta
    # target = (87, 113, 46)

    w1 = 0.3
    w2 = 0.6
    w3 = 0.1

    # 计算混合颜色
    target_color = find_target_iter(rgb1, rgb2, rgb3, w1, w2, w3)
    print(f"Target color: {target_color}")

    # 绘制输入颜色和混合颜色
    fig, ax = plt.subplots(1, 4, figsize=(12, 3))

    colors = [rgb1, rgb2, rgb3, target_color]
    titles = ['RGB1', 'RGB2', 'RGB3', 'Mixed Color']
    weights = [w1, w2, w3]

    # 调用绘图函数
    plot_colors_with_weights(ax, colors, titles, weights)

    plt.show()
