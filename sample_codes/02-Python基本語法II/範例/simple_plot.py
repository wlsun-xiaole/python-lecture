import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 要視覺化的資料 (0~2 之間的 sin 函式)
# 使用 numpy 來產生
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# 使用 matplotlib 設定圖片
plt.title('A simple sin(x) plot') # 設定圖片標題
plt.xlabel('x') # 設定 x 軸標籤
plt.ylabel('sin(x)') # 設定 y 軸標籤
plt.grid() # 加上格線
plt.plot(t, s) # 設定 x 和 y 軸的資料
plt.show() # 顯示圖片
