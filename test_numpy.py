import numpy as np

import matplotlib.pyplot as plt
def plot_grid(Xs, Ys, axs=None):
    t = np.arange(Xs.size) # define progression of int for indexing colormap
    if axs:
        axs.plot(0, 0, marker='*', markersize=7, color='r', linestyle='none') #plot origin
        axs.scatter(Xs,Ys, c=t, cmap='jet', marker='o') # scatter x vs y
        axs.axis('scaled') # axis scaled
    else:
        plt.plot(0, 0, marker='*', color='r',markersize=7, linestyle='none') #plot origin
        plt.scatter(Xs,Ys, c=t, cmap='jet', marker='o') # scatter x vs y
        plt.axis('scaled') # axis scaled
        plt.show()
# let's see it with numpy
nX, nY, res = 10, 10, 21 # boundary of our space + resolution
X = np.linspace(-nX, +nX, res) # give me 21 points linear space from -10, +10
Y = np.linspace(-nX, +nX, res) # give me 21 points linear space from -10, +10
# meshgrid is very useful to evaluate functions on a grid
# z = f(X,Y)
# please see https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
Xs, Ys = np.meshgrid(X, Y) #NxN, NxN
plot_grid(Xs, Ys)
#plt.imshow(Ys, cmap='jet')