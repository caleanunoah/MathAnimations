import matplotlib.pyplot as plt
import numpy as np
from math import pi


def setup2D():
    # Set up the figure
    plt.clf()
    plt.setp(plt.gca())

    # Make two subplots for explaining sine + cosine relation to circles
    fig, axs = plt.subplots(2, 2)
    plt.close(1)  # keep me for only one window open at a time

    # set up functions to be plotted
    w_line = np.linspace(0, 2 * pi, 100)
    y1_line = np.cos(w_line)
    y2_line = np.sin(w_line)

    # set up the axis
    line = np.linspace(-2, 2, 100)
    lin2 = np.zeros(100)
    lin3 = np.linspace(0, 2 * pi, 100)
    color_vertical = np.linspace(-1, 1, 100)
    color_horizontal = np.linspace(1, -1, 100)

    # Plot origin for circle (visually more appealing)
    axs[0, 1].set(xlim=(-3, 3), ylim=(-2, 2))

    # Add some axes outline for visual aid
    axs[0, 0].plot(line, lin2, color="#d6d6d6")
    axs[0, 0].plot(lin2, line, color="#d6d6d6")  # vertical line --circle

    # Plot gray outline of sine
    axs[0, 1].plot(w_line, y2_line, '#d6d6d6')  # sine
    axs[0, 1].set(xlim=(0, 2 * pi), ylim=(-2, 2))  # sine

    # Plot gray outline of cosine
    axs[1, 0].plot(y1_line, w_line, '#d6d6d6')  # cosine
    axs[1, 0].set(xlim=(-2, 2), ylim=(2 * pi, 0))  # cosine

    # Write welcome message.
    #axs[1, 1].text(x=0.2, y=0.8, s="Click to continue.")

    return [fig, axs, line, lin2, w_line, y1_line, y2_line]


def setup3D():
    # Set up the figure
    #plt.clf()
    #plt.setp(plt.gca())

    # Make two subplots for explaining sine + cosine relation to circles
    # fig, axs = plt.subplots(2, 2)
    fig = plt.figure()
    fig.suptitle('Euler in 3D', fontsize=16)
    # Create subplots
    ax = fig.add_subplot(2, 2, 1, projection='3d')
    ax3 = fig.add_subplot(223, projection='3d')
    ax4 = fig.add_subplot(224, projection='3d')

    # Title both subplots
    # ax.set_title("3D Euler")  # right plot
    ax3.set_title("Sine View")  # right plot
    ax4.set_title("Cosine View")  # left plot

    ax3.view_init(0, 0)  # sine view
    ax4.view_init(0, 90)  # cosine view

    # set up the x and y for the euler animation
    z_line = np.linspace(0, 2 * pi, 100)
    x_line = np.cos(z_line)
    y_line = np.sin(z_line)

    # Draw an origin on both. Connects the subplots relative to each other
    ax.scatter3D(xs=0, ys=0, zs=0)
    ax3.scatter3D(xs=0, ys=0, zs=0)
    ax4.scatter3D(xs=0, ys=0, zs=0)

    plt.waitforbuttonpress()
    ax.plot3D(x_line, y_line, z_line, '#d6d6d6')
    ax3.plot3D(x_line, y_line, z_line, '#d6d6d6')
    ax4.plot3D(x_line, y_line, z_line, '#d6d6d6')
    return [ax, ax3, ax4, x_line, y_line, z_line]
