#func: 生成子视图
import matplotlib.pyplot as plt

plt.figure()

"""
# 画 2*2的subplot
plt.subplot(2, 2, 1)
# plot([x1, x2],[y1, y2])
plt.plot([0, 1],
         [0, 1])

plt.subplot(2, 2, 2)
plt.plot([0, 1],
         [1, 0])

plt.subplot(2, 2, 3)
plt.plot([1, 0],
         [1, 0])

plt.subplot(2, 2, 4)
plt.plot([0, 1],
         [1, 0])
"""

plt.subplot(2, 1, 1)
# plot([x1, x2],[y1, y2])
plt.plot([0, 1],
         [0, 1])
# 这里的4 是因为上面占完一行有3个小块所以从4开始
plt.subplot(2, 3, 4)
plt.plot([0, 1],
         [1, 0])

plt.subplot(2, 3, 5)
plt.plot([1, 0],
         [1, 0])

plt.subplot(2, 3, 6)
plt.plot([0, 1],
         [1, 0])

plt.show()