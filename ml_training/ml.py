from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_colors_with_weights(ax, colors, titles, weights=None):
    for i, (color, title) in enumerate(zip(colors, titles)):
        ax[i].set_title(title)
        ax[i].add_patch(patches.Rectangle((0, 0), 1, 1, color=tuple(c / 255 for c in color)))
        if weights is not None and i < len(weights):  # 仅对前三个颜色显示权重
            ax[i].text(0.5, -0.1, f'w{i + 1} = {weights[i]:.2f}', ha='center', va='center', transform=ax[i].transAxes)
        ax[i].axis('off')

data_path = "target_color_dataset.csv"  # 替换为实际路径
data = pd.read_csv(data_path)

# 特征工程：选择输入（4种颜色的RGB）和输出（w1）
X = data[["rgb1_r", "rgb1_g", "rgb1_b",
        "rgb2_r", "rgb2_g", "rgb2_b",
        "rgb3_r", "rgb3_g", "rgb3_b",
        "target_r", "target_g", "target_b"]]
y = data["w1"]

# 数据拆分为训练集（10%）、验证集（10%）、测试集（80%）
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.9, random_state=42)  # 10% 训练集
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=8/9, random_state=42)  # 10% 验证集，80% 测试集

# 初始化随机森林模型
model = RandomForestRegressor(
    n_estimators=5,       # 减少树的数量，确保 C++ 转换的代码简单
    max_depth=10,           # 限制深度以减少生成代码的复杂性
    random_state=42
)

# 训练模型
model.fit(X_train, y_train)

# 保存模型
model_save_path = "models/random_forest_model.pkl"
joblib.dump(model, model_save_path)
print(f"Model saved to {model_save_path}")

# 验证集评估
y_val_pred = model.predict(X_val)
val_loss = mean_squared_error(y_val, y_val_pred)
val_mae = mean_absolute_error(y_val, y_val_pred)
print(f"Validation Loss (MSE): {val_loss}")
print(f"Validation MAE: {val_mae}")

# 测试集评估
y_test_pred = model.predict(X_test)
test_loss = mean_squared_error(y_test, y_test_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)
print(f"Test Loss (MSE): {test_loss}")
print(f"Test MAE: {test_mae}")


# 加载已保存的模型
model = joblib.load(model_save_path)
print(f"Model loaded from {model_save_path}")

rgb1 = (0, 33, 133)  # blue
rgb2 = (252, 211, 0)  # yellow
rgb3 = (3, 211, 252)  # cyan
target_rgb = (87, 113, 46)

# 将输入数据转换为 DataFrame 格式
input_data = pd.DataFrame([[
    *rgb1, *rgb2, *rgb3, *target_rgb
]], columns=["rgb1_r", "rgb1_g", "rgb1_b",
                "rgb2_r", "rgb2_g", "rgb2_b",
                "rgb3_r", "rgb3_g", "rgb3_b",
                "target_r", "target_g", "target_b"])

# 使用模型预测权重
weights = model.predict(input_data).flatten()
print(weights)
print(f"Computed Weight: w1={weights[0]:.2f}")

# 绘制输入颜色和目标颜色
fig, ax = plt.subplots(1, 4, figsize=(12, 3))

colors = [rgb1, rgb2, rgb3, target_rgb]
titles = ['RGB1', 'RGB2', 'RGB3', 'Target Color']

# 调用绘图函数
plot_colors_with_weights(ax, colors, titles, weights)

plt.show()
