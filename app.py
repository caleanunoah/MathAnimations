from mpl_toolkits import mplot3d
import time
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")
# Set the rotation for interactive 3D plot
# ax.azim = 60

# Draw the Euler function helix
z_line = np.linspace(0, 10, 100)
x_line = np.cos(z_line)
y_line = np.sin(z_line)
ax.plot3D(x_line, y_line, z_line, 'gray')
ax.set_title("Euler's Formula in 3D")

for i in range(0, len(x_line)-1):
    #ax.plot3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], [z_line[i], z_line[i + 1]], 'gray')
    ax.scatter3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], [z_line[i], z_line[i + 1]], c= [z_line[i], z_line[i + 1]], cmap="Greens");
    plt.pause(0.05)

plt.show()








