# func:主次坐标轴
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1

fig, ax1 = plt.subplots()
# 依赖同样的x轴生成不同的y轴
ax2 = ax1.twinx()
ax1.plot(x, y1, 'b-')
ax2.plot(x, y2, 'r-')

ax1.set_xlabel("X data")
ax1.set_ylabel("Y1")
ax2.set_ylabel("Y2")
plt.show()