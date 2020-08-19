import matplotlib.pyplot as plt
from functions.graph2D import graph2D
from functions.graph3D import graph3D
from functions.setup_graphs import setup2D, setup3D

# Set up a plot, figure, the initial colors
[fig, axs, line, lin2, w_line, y1_line, y2_line] = setup2D()


# wait for user input
plt.waitforbuttonpress()

# If user clicks on figure, draw out 2D Euler relation
# Notice the relationship between Sine's amplitude and the y-coordinate of the unit circle.
# Likewise, notice the relationship between Cosine's amplitude and the x-coordinate of the unit circle
while True:
    # Graph the Euler Relation in 2D
    fig.suptitle('Euler in 2D', fontsize=16)

    graph2D(axs, line, lin2, w_line, y1_line, y2_line)
    fig.tight_layout()
    #plt.show()
    print("Finished 2D Animation")

    plt.waitforbuttonpress()

    [ax, ax3, ax4, x_line, y_line, z_line] = setup3D()

    while True:
        # Now set up the 3D case
        # [ax, ax3, ax4, x_line, y_line, z_line] = setup3D()
        graph3D(plt, ax, ax3, ax4, x_line, y_line, z_line)
        plt.show()
        break

    break
