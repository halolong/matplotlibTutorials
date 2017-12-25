# func: Bar
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
# 生成均匀分布的数据(generate uniform distribution)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)


plt.bar(X, +Y1, facecolor='#9ca4ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ffa59c', edgecolor='white')

plt.xlim((-2, n))
plt.ylim((-1, 1))

# 添加annotation
for x,y in zip(X, Y1):
    # ha = horizontal alignment
    # va = vertical alignment
    plt.text(x, y + 0.02, '%.2f'%y, ha='center', va='bottom')

for x,y in zip(X, Y2):
    # ha = horizontal alignment
    # va = vertical alignment
    plt.text(x, -y - 0.02, '-%.2f'%y, ha='center', va='top')

plt.xticks()
plt.yticks()

plt.show()