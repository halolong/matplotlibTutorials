# func: 生成3D图像 (plotting 3D image)
import matplotlib.pyplot as plt
import numpy as np
from  mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

# X,Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
print(X)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)

# height
Z = np.sin(R)

# drawing 3d
# rstride 表示(row)行的跨度大小 cstride 表示(column)列的跨度
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap("rainbow"))

# 添加底部的等高线图
ax.contourf(X, Y, Z, zdir='z', offset=-1, cmap=plt.get_cmap("rainbow"))
ax.set_zlim((-2, 2))
plt.show()