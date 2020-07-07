import time
import numpy as np
from funcs import display_funcs
import matplotlib.pyplot as plt
from math import pi


def tellme(s):
    print(s)
    plt.title(s, fontsize=12)
    plt.draw()


# Set up the figure
plt.clf()
plt.setp(plt.gca())

# Make two subplots for explaining sine + cosine relation to circles
fig, axs = plt.subplots(2, 2)

w_line = np.linspace(0, 2 * pi, 100)
y1_line = np.cos(w_line)
y2_line = np.sin(w_line)

# Plot origins
axs[0, 0].scatter(x=0, y=0)
#axs[1, 0].scatter(x=0, y=0)
# Plot gray outline of circles to be traced
#axs[0, 0].plot(np.cos(w_line), np.sin(w_line), 'gray')
#axs[1, 0].plot(np.cos(w_line), np.sin(w_line), 'gray')
# Plot gray outline of sine and cosine waves to be traced
axs[0, 1].plot(w_line, y2_line, 'gray' ) #  SINE
#axs[0, 1].set(xlim=(-1, 1 ), ylim=(-1, 1 ))
# Set the axis limits to +/-1
axs[1, 0].plot(w_line, y1_line, 'gray' ) #  COSINE
#axs[1, 1].set(xlim=(-1, 1 ), ylim=(-1, 1 ))

plt.waitforbuttonpress()
#plt.close(1)

while True:
    #axs[0, 0].plot(np.cos(w_line), np.sin(w_line), 'green')
    #axs[0, 1].plot(np.cos(w_line), 'red')

    for i in range(0, len(w_line) - 1):
        # top circle
        axs[0, 0].plot(np.cos([w_line[i], w_line[i + 1]]), np.sin([w_line[i], w_line[i + 1]]), 'green')
        axs[0, 0].axis('equal')
        axs[0, 0].set(xlim=(-3 , 3), ylim=(-2 , 2))
        # bottom circle
        #axs[1, 0].plot(np.cos([w_line[i], w_line[i + 1]]), np.sin([w_line[i], w_line[i + 1]]), 'green')
        #axs[1, 0].axis('equal')
        #axs[1, 0].set(xlim=(-3 , 3), ylim=(-2 , 2))
        # Plot the cosine
        """axs[1, 0].plot([w_line[i], w_line[i + 1]], [y1_line[i], y1_line[i + 1]], 'red' )
        axs[1, 0].axis('equal')
        axs[0, 0].set(xlim=(-3, 3), ylim=(-2, 2))"""
        axs[1, 0].plot([w_line[i], w_line[i + 1]], [y1_line[i], y1_line[i + 1]], 'red')
        axs[1, 0].axis('equal')
        #axs[1, 0].set(xlim=(0, 2*pi), ylim=(-1, 1))
        # Plot the sine
        axs[0, 1].plot([w_line[i], w_line[i + 1]], [y2_line[i], y2_line[i + 1]], 'black' )
        axs[0, 1].axis('equal')
        #axs[0, 1].set(xlim=(0, 2*pi), ylim=(-1, 1))
        plt.pause(0.05)
    fig.tight_layout()
    plt.show()
    plt.close(1)
    #break;

# Plot cosine animation on row 2
axs[1, 0].scatter(x=0, y=0)
axs[1, 0].plot(np.cos(w_line), np.sin(w_line), 'green')
axs[1, 1].plot(np.sin(w_line), 'blue')

#display_funcs.tellme(plt, 'Remember Sine and Cosine? Click to continue...')
plt.waitforbuttonpress()

while True:
    # Set up plots
    plt.close(1)
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    #ax2 = fig.add_subplot(1, 2, 1, projection='3d')

    # set up the x and y for the euler animation
    z_line = np.linspace(0, 10, 100)
    x_line = np.cos(z_line)
    y_line = np.sin(z_line)

    # Title both subplots
    ax.set_title("Euler's Formula 3D")  # right plot
    #ax2.set_title("Euler's Formula 2D")  # left plot

    # Draw an origin on both. Connects the subplots relative to each other
    ax.scatter3D(xs=0, ys=0, zs=0)
    #ax2.scatter3D(xs=0, ys=0, zs=0)

    plt.waitforbuttonpress()
    ax.plot3D(x_line, y_line, z_line, 'gray')

    while True:
        # Now go through and superimpose a scatter on top the Euler function helix
        for i in range(0, len(x_line) - 1):
            ax.scatter3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], [z_line[i], z_line[i + 1]],
                         c=[z_line[i], z_line[i + 1]], cmap="Greens");
            ax.plot3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], 0, 'green');
            plt.pause(0.05)

        plt.show()
        break;
    break;
#break

# Keep plot up until user exits, without it automatically closes after 2 mouse clicks
plt.show()




