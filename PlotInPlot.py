# func: 图中图(plot in plot)
import matplotlib.pyplot as plt

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 5, 2, 8, 6]

# 设置相对位置 离左边10%,底部10%,整个大小占80% * 80%
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
# ax1.set_ylabel()
ax1.set_xlabel("I'm ax2 X")
ax1.set_ylabel("I'm ax2 Y")
ax1.plot(x, y, 'r')

left, bottom, width, height = 0.2, 0.6, 0.2, 0.2
ax2 = fig.add_axes([left, bottom, width, height])
ax2.set_xlabel("I'm ax2 X")
ax2.set_ylabel("I'm ax2 Y")
ax2.plot(x, y)



# method 2:直接用plt画
plt.axes([0.7, 0.2, 0.2, 0.2])
plt.plot(y[::-1], x, 'g')
plt.xlabel("I'm ax3 X")
plt.ylabel("I'm ax3 Y")

plt.show()