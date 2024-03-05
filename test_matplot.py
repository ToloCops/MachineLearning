import matplotlib
import matplotlib.pyplot as plt
import numpy as np
v = np.array([2.5, 3.2])
# all the X first, then all the Y
# [X1 X2] [Y1 Y2]
plt.plot([0, v[0]], [0, v[1]],
    marker='x', color='red', lw=4,
    markersize=6)
plt.axis('equal')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Vector")
plt.annotate('(0, 0)', xy=(0, 0), xytext=(.1, -.3))
plt.annotate(f'({v[0]},{v[1]})', xy=(v[0], v[1]), xytext=(v[0], v[1]))
plt.axis([-5, 5, -5, 5])
plt.show()