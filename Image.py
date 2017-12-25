# func:展示图像(show image)
import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)

"""
关于其值表示出来的意思解释请参照下面的网址
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
for the value of "origin"= ['upper', 'lower'], check this:
http://matplotlib.org/examples/pylab_examples/image_origin.html
"""

# upper 一一对应上面的值，lower与数据相反
plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
# shrink 调整colorbar的比例
plt.colorbar(shrink=0.9)



plt.xticks(())
plt.yticks(())
plt.show()