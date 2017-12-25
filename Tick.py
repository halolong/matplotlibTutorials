# func: 防止数据遮挡其坐标轴
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=20, zorder=1)      # set zorder for ordering the plot in plt 2.0.2 or higher
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    # 设置坐标轴x和y上所有的点的样式
    label.set_bbox(dict(facecolor='red',edgecolor='None',alpha=0.5))


plt.show()