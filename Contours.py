# func: 等高线图(contour)
import matplotlib.pyplot as plt
import numpy as np

def height(x, y):
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

X,Y = np.meshgrid(x, y)

# 填充颜色到等高线(use plt.contourf to filling contours)  这里的第三个参数代表色差数+2:0代表2个颜色，8则是10
plt.contourf(X, Y, height(X, Y), 8, alpha=0.85, cmap=plt.cm.hot)

# 添加边界线 use plt.contour to add contour lines
C = plt.contour(X, Y, height(X, Y), 8, colors='black', linewidths=1)

# adding label
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()