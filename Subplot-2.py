import matplotlib.pyplot as plt
import  matplotlib.gridspec as gridspec

# method1:subplot2grid
plt.figure(num=1)
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
ax1.plot([1, 2],
         [1, 2]
         )
ax1.set_title("ax1_title")

# colspan,rowspan(default=1) ax2指第二行从最左边开始占两列
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (2, 0))
ax4 = plt.subplot2grid((3, 3), (2, 1))
ax5 = plt.subplot2grid((3, 3), (1, 2), rowspan=3)


# method2:gridspec ####
plt.figure(num=2)
gs = gridspec.GridSpec(3, 3)
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])


# method3: easy to define structure

f,((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)

ax11.scatter([1, 2],
             [1, 2])
plt.tight_layout()

plt.show()