# func: 添加Lengend
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

# set figure 3
plt.figure()

# set range
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# set label
plt.xlabel("I am X")
plt.ylabel("I am Y")

# set another range
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)

plt.yticks([-2, -1.8, 1.1, 3],
           [r'$not\ bad$', r'$bad \alpha$', r'$good$', r'$great$'])

l1 = plt.plot(x, y2, label='up')
l2 = plt.plot(x, y1, color='red', linewidth=1.0, linestyle=':', label='down')

plt.legend(loc='best', shadow=True,)

plt.show()
