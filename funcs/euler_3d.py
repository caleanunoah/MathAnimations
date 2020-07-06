import numpy as np


def euler_3d(plt, w_line, y2_line):
    plt.plot(w_line, y2_line, 'red', label="cosine")
    plt.pause(1)
    # break

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