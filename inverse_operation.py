from scipy.optimize import minimize
import mixbox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def find_weights(rgb1, rgb2, rgb3, target_rgb):
    """
    给定三种输入颜色和目标颜色，求解满足非负和归一约束的权重。
    参数:
    - rgb1, rgb2, rgb3: 输入的三个 RGB 颜色 (tuple, e.g., (R, G, B))
    - target_rgb: 目标 RGB 颜色 (tuple, e.g., (R, G, B))
    返回:
    - weights: 混合权重列表 (list, e.g., [w1, w2, w3])
    """
    # 转换 RGB 到 latent 空间
    z1 = np.array(mixbox.rgb_to_latent(rgb1))
    z2 = np.array(mixbox.rgb_to_latent(rgb2))
    z3 = np.array(mixbox.rgb_to_latent(rgb3))
    z_target = np.array(mixbox.rgb_to_latent(target_rgb))

    # 定义目标函数：最小化 || w1*z1 + w2*z2 + w3*z3 - z_target ||^2
    def objective(w):
        return np.linalg.norm(w[0] * z1 + w[1] * z2 + w[2] * z3 - z_target)

    # 初始值
    initial_weights = [1 / 3, 1 / 3, 1 / 3]

    # 定义约束条件
    constraints = [
        {"type": "eq", "fun": lambda w: np.sum(w) - 1},  # w1 + w2 + w3 = 1
    ]
    bounds = [(0, 1), (0, 1), (0, 1)]  # w1, w2, w3 >= 0 且 <= 1

    # 优化求解
    result = minimize(objective, initial_weights, constraints=constraints, bounds=bounds)
    if result.success:
        return result.x
    else:
        raise ValueError("优化未能成功求解")


def plot_colors_with_weights(ax, colors, titles, weights=None):
    for i, (color, title) in enumerate(zip(colors, titles)):
        ax[i].set_title(title)
        ax[i].add_patch(patches.Rectangle((0, 0), 1, 1, color=tuple(c / 255 for c in color)))
        if weights is not None and i < len(weights):  # 仅对前三个颜色显示权重
            ax[i].text(0.5, -0.1, f'w{i + 1} = {weights[i]:.2f}', ha='center', va='center', transform=ax[i].transAxes)
        ax[i].axis('off')

# 示例调用
if __name__ == "__main__":
    rgb1 = (0, 33, 133)  # blue
    rgb2 = (252, 211, 0)  # yellow
    rgb3 = (3, 211, 252)  # cyan
    target_rgb = (76, 168, 52)

    # 求解权重
    weights = find_weights(rgb1, rgb2, rgb3, target_rgb)
    print(f"Computed Weights: w1={weights[0]:.2f}, w2={weights[1]:.2f}, w3={weights[2]:.2f}")

    # 绘制输入颜色和目标颜色
    fig, ax = plt.subplots(1, 4, figsize=(12, 3))

    colors = [rgb1, rgb2, rgb3, target_rgb]
    titles = ['RGB1', 'RGB2', 'RGB3', 'Target Color']

    # 调用绘图函数
    plot_colors_with_weights(ax, colors, titles, weights)

    plt.show()