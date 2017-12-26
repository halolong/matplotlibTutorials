# func:动画
import numpy as np
from  matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
# 线条的值是按正弦函数变化 这里的逗号是获取返回列表的第一个值
line, = ax.plot(x, np.sin(x))
# 表示变化动画的值


def animate(i):
    line.set_ydata(np.sin(x+i/30))
    return line,


# 表示初始位置
def init():
    line.set_ydata(np.sin(x))
    return line,


ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=True)

plt.show()