import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

# set figure 3
plt.figure()
plt.plot(x, y2)
# set style
plt.plot(x, y1, color='red', linewidth=1.0, linestyle=':')

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

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# set origin of coordinate
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.show()
