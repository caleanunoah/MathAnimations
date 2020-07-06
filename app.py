import time

import numpy as np
import matplotlib.pyplot as plt
from math import pi

def tellme(s):
    print(s)
    plt.title(s, fontsize=12)
    plt.draw()


plt.clf()
plt.setp(plt.gca())

tellme('Welcome, click to begin')

plt.waitforbuttonpress()

while True:
    w_line = np.linspace(0, 2 * pi, 100);
    y1_line = np.sin(w_line)
    y2_line = np.cos(w_line)
    plt.plot(w_line, y1_line, 'red', label="sin")
    plt.plot(w_line, y2_line, 'black', label="cosine")

    tellme('Remember Sine and Cosine? Click for yes')
    plt.waitforbuttonpress()

    while True:
        plt.plot(w_line, y2_line, 'red', label="cosine")
        plt.pause(1)
        #break

        # Set up plots
        fig = plt.figure()
        ax = fig.add_subplot(1, 2, 2, projection='3d')
        ax2 = fig.add_subplot(1, 2, 1, projection='3d')
        # ax = plt.axes(projection="3d")
        # Set the rotation for interactive 3D plot

        # set up the x and y for the
        z_line = np.linspace(0, 10, 100)
        x_line = np.cos(z_line)
        y_line = np.sin(z_line)

        # Title both subplots
        ax.set_title("Euler's Formula 3D")
        ax2.set_title("Euler's Formula 2D")

        # Draw an origin on both. Connects the subplots relative to each other
        ax.scatter3D(xs=0, ys=0, zs=0)
        ax2.scatter3D(xs=0, ys=0, zs=0)

        plt.waitforbuttonpress()
        ax.plot3D(x_line, y_line, z_line, 'gray')

        while True:
            # Now go through and superimpose a scatter ontop the Euler function helix
            for i in range(0, len(x_line) - 1):
                ax.scatter3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], [z_line[i], z_line[i + 1]],
                             c=[z_line[i], z_line[i + 1]], cmap="Greens");
                ax.plot3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], 0, 'blue');
                plt.pause(0.05)

            plt.show()
            break;
        break;
    break

# Keep plot up until user exits, without it automatically closes after 2 mouse clicks
plt.show()




