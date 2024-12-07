import os
import joblib
import numpy as np
from tensorflow.keras.models import load_model

def find_weights(rgb1, rgb2, rgb3, target_rgb, model_path, scaler_path):
    """
    根据输入的 RGB 特征，预测 w1, w2, 和 w3。

    参数:
        rgb1 (list): 第一个 RGB 值 [r, g, b]。
        rgb2 (list): 第二个 RGB 值 [r, g, b]。
        rgb3 (list): 第三个 RGB 值 [r, g, b]。
        target_rgb (list): 目标 RGB 值 [r, g, b]。
        model_path (str): 保存的模型文件路径。
        scaler_path (str): 保存的标准化器文件路径。

    返回:
        tuple: 预测的权重 (w1, w2, w3)。
    """
    # 检查文件路径是否存在
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    if not os.path.exists(scaler_path):
        raise FileNotFoundError(f"Scaler file not found at {scaler_path}")

    # 加载标准化器和模型
    scaler = joblib.load(scaler_path)
    model = load_model(model_path)

    # 将输入拼接成一个扁平数组
    rgb_values = rgb1 + rgb2 + rgb3 + target_rgb
    rgb_values = np.array(rgb_values).reshape(1, -1)

    # 标准化输入
    rgb_values_scaled = scaler.transform(rgb_values)

    # 预测
    predicted_weights = model.predict(rgb_values_scaled).flatten()

    # 计算 w3
    w1, w2 = predicted_weights
    w3 = 1 - w1 - w2

    # 返回结果
    return w1, w2, w3

# Example usage (delete this section for the actual library file):
if __name__ == "__main__":
    # 定义测试输入
    rgb1 = (0, 33, 133)  # blue
    rgb2 = (252, 211, 0)  # yellow
    rgb3 = (3, 211, 252)  # cyan
    target_rgb = (76, 168, 52)

    project_path = "D:\\Feifan\\Desktop\\DE2\\Physical Computing\\Gizmo\\Gizmo-Project"  # 替换为你的工程路径
    model_dir = os.path.join(project_path, "models")

    model_path = os.path.join(model_dir, "mlp_model.h5")
    scaler_path = os.path.join(model_dir, "scaler.pkl")

    # 调用预测函数
    try:
        w1, w2, w3 = find_weights(rgb1, rgb2, rgb3, target_rgb, model_path, scaler_path)
        print(f"Predicted weights: w1={w1}, w2={w2}, w3={w3}")
    except Exception as e:
        print(f"Error: {e}")
