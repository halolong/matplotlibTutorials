# func: figure的基本用法
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

# set figure 1
plt.figure(num=1)
plt.plot(x, y1)

# set figure 3
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
# set style
plt.plot(x, y1, color='red', linewidth=1.0, linestyle=':')

plt.show()
