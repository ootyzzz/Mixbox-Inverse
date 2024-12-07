import mixbox_3
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def rgb_iter(rgb1, rgb2, rgb3, w1, w2, w3):
    def mix_two_colors(color1, color2, weight1, weight2):
        return [
            round(color1[i] - (color1[i] - color2[i]) * (1 - weight1))
            for i in range(3)
        ]

    # 先混合前两种颜色
    mixed_color = mix_two_colors(rgb1, rgb2, w1, w2)
    
    # 再将混合后的颜色与第三种颜色混合
    final_color = mix_two_colors(mixed_color, rgb3, (w1 + w2), w3)
    
    return final_color

def cym(rgb1, rgb2, rgb3, w1, w2, w3):
    def rgb_to_cym(rgb):
        r, g, b = rgb
        c = 255 - r
        y = 255 - g
        m = 255 - b
        return (c, y, m)

    def cym_to_rgb(cym):
        c, y, m = cym
        r = 255 - c
        g = 255 - y
        b = 255 - m
        return (r, g, b)
    
    # 将RGB转换为CYM
    cym1 = rgb_to_cym(rgb1)
    cym2 = rgb_to_cym(rgb2)
    cym3 = rgb_to_cym(rgb3)

    # 直接加权计算混合颜色
    c_mixed = round((cym1[0] * w1 + cym2[0] * w2 + cym3[0] * w3) / (w1 + w2 + w3))
    y_mixed = round((cym1[1] * w1 + cym2[1] * w2 + cym3[1] * w3) / (w1 + w2 + w3))
    m_mixed = round((cym1[2] * w1 + cym2[2] * w2 + cym3[2] * w3) / (w1 + w2 + w3))

    # 将混合后的CYM转换回RGB
    final_color = cym_to_rgb((c_mixed, y_mixed, m_mixed))
    
    return final_color

def plot_colors_with_weights(ax, colors, titles, weights=None):
    for i, (color, title) in enumerate(zip(colors, titles)):
        ax[i].set_title(title)
        ax[i].add_patch(patches.Rectangle((0, 0), 1, 1, color=tuple(c / 255 for c in color)))
        if weights is not None and i < len(weights):  # 仅对前三个颜色显示权重
            ax[i].text(0.5, -0.1, f'w{i + 1} = {weights[i]:.2f}', ha='center', va='center', transform=ax[i].transAxes)
        ax[i].axis('off')

if __name__ == "__main__":
    # 示例调用
    rgb1 = (0, 33, 133)  # blue
    rgb2 = (252, 211, 0) # yellow
    rgb3 = (255, 0, 255) # magenta

    w1 = 0.3
    w2 = 0.6
    w3 = 0.1

    result = cym(rgb1, rgb2, rgb3, w1, w2, w3)
    print(result)  # 输出混合后的颜色值

        # 计算混合颜色
    target_color = cym(rgb1, rgb2, rgb3, w1, w2, w3)
    print(f"Target color: {target_color}")

    # 绘制输入颜色和混合颜色
    fig, ax = plt.subplots(1, 4, figsize=(12, 3))

    colors = [rgb1, rgb2, rgb3, target_color]
    titles = ['RGB1', 'RGB2', 'RGB3', 'Mixed Color']
    weights = [w1, w2, w3]

    # 调用绘图函数
    plot_colors_with_weights(ax, colors, titles, weights)

    plt.show()
