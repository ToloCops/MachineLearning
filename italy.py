from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('figs/italy.png')
im = np.array(img)
X, Y = np.where(im != 0)
sampling = 100 # to have less points
X, Y = X[::sampling], Y[::sampling]

fig = plt.scatter(X, Y, c=X, marker='o', cmap='jet')
plt.scatter(0, 0, c='red')
_ = plt.axis('scaled')
plt.show()

