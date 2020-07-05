from mpl_toolkits import mplot3d
import time
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")
# Set the rotation for interactive 3D plot
# ax.azim = 60

# Draw the Euler function helix
#z_line = np.linspace(0, 10, 100)
#x_line = np.cos(z_line)
#y_line = np.sin(z_line)
#ax.plot3D(x_line, y_line, z_line, 'gray')

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 4, 5, 6, 7, 8, 9, 10]
z = [5, 6, 7, 8, 9, 10, 11, 12]

for i in range(0, len(x)-1):
    print("X values in this iteration")
    print(x[i])
    print(x[i+1])
    print("Y values in this iteration")
    print(y[i])
    print(y[i + 1])
    print("Z values in this iteration")
    print(z[i])
    print(z[i + 1])
    ax.plot3D([x[i], x[i+1]], [y[i], y[i+1]], [z[i], z[i+1]], 'gray')
    plt.pause(0.05)

plt.show()
#ax.plot3D(x, y, z, 'gray')

#ax.scatter3D(x_line, y_line, z_line, c=z_line );

#ax.set_title("Euler's Formula in 3D")







