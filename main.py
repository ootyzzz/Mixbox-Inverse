from forward_operation import find_target_color
from inverse_operation import find_weights
import random
import numpy as np
from prettytable import PrettyTable

def compare_operations(rgb1, rgb2, rgb3, w1, w2, w3):
    """
    比较单次正向和逆向运算结果，返回详细记录。
    """
    # 正向运算
    target_color = find_target_color(rgb1, rgb2, rgb3, w1, w2, w3)

    # 逆向运算
    computed_weights = find_weights(rgb1, rgb2, rgb3, target_color)

    # 计算误差
    original_weights = [w1, w2, w3]
    diff = [abs(ow - cw) for ow, cw in zip(original_weights, computed_weights)]

    return {
        "RGB1": rgb1,
        "RGB2": rgb2,
        "RGB3": rgb3,
        "Target Color": target_color,
        "Original Weights": original_weights,
        "Computed Weights": computed_weights.tolist(),
        "Difference": diff,
    }

def batch_test(num_tests=10):
    """
    批量测试正向和逆向运算，生成随机初始条件并记录结果。
    """
    results = []
    for test_idx in range(num_tests):
        # 随机生成 RGB 颜色
        rgb1 = (255, 0, 0)  # Red
        rgb2 = (0, 255, 0)  # Green
        rgb3 = (0, 0, 255)  # Blue

        # 随机生成权重并归一化
        w1, w2, w3 = np.random.rand(3)
        total_weight = w1 + w2 + w3
        w1, w2, w3 = w1 / total_weight, w2 / total_weight, w3 / total_weight

        # 运行对比
        result = compare_operations(rgb1, rgb2, rgb3, w1, w2, w3)
        results.append(result)

    # 打印汇总结果
    print("\n===== Summary =====")
    table = PrettyTable()
    table.field_names = [
        "Test",
        "Target Color",
        "Original Weights",
        "Computed Weights",
        "Difference",
    ]

    for i, result in enumerate(results):
        target_color = result["Target Color"]
        original_weights = [f"{w:.3f}" for w in result["Original Weights"]]
        computed_weights = [f"{w:.3f}" for w in result["Computed Weights"]]
        difference = [f"{d:.3f}" for d in result["Difference"]]

        table.add_row(
            [
                i + 1,
                f"{target_color}",
                original_weights,
                computed_weights,
                difference,
            ]
        )
    print(table)
    return results

if __name__ == "__main__":
    # 批量运行测试
    num_tests = 10  # 设置测试数量
    batch_test(num_tests)
