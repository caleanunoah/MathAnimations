def graph3D(plt, ax, ax3, ax4, x_line, y_line, z_line):
    # Now go through and superimpose a scatter on top the Euler function helix
    for i in range(0, len(x_line) - 1):
        # Plot the 3D Euler
        ax.scatter3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], [z_line[i], z_line[i + 1]],
                     c=[z_line[i], z_line[i + 1]], cmap="Greens")
        ax.plot3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], 0, 'green')

        # Plot the Sine View
        ax3.scatter3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], [z_line[i], z_line[i + 1]],
                      c=[z_line[i], z_line[i + 1]], cmap="Greens")
        ax3.plot3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], 0, 'green')

        # Plot the Cosine View
        ax4.scatter3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], [z_line[i], z_line[i + 1]],
                      c=[z_line[i], z_line[i + 1]], cmap="Greens")
        ax4.plot3D([x_line[i], x_line[i + 1]], [y_line[i], y_line[i + 1]], 0, 'green')

        plt.pause(0.01)
