import numpy as np
import matplotlib.pyplot as plt


def graph2D(axs, line, lin2, w_line, y1_line, y2_line):
    for i in range(0, len(w_line) - 1):
        # Redraw axis in gray again
        axs[0, 0].plot(lin2, line, color="#d6d6d6")  # vertical line --circle
        axs[0, 0].plot(line, lin2, color="#d6d6d6")  # horizontal line --circle

        # draw the axis color updates based on where the ball is on the sin (vertical blue) and cos (horizontal)
        color_vertical = np.linspace(0, np.sin([w_line[i], w_line[i + 1]]), 100)
        color_horizontal = np.linspace(1, np.cos([w_line[i], w_line[i + 1]]), 100)

        axs[0, 0].plot(lin2, color_vertical, color="#1c8eff")  # changing vertical blue line
        axs[0, 0].plot(color_horizontal, lin2, color="#ffdd1c")  # changing horizontal yellow line

        # draw a ball that will trace circle
        axs[0, 0].scatter(np.cos([w_line[i], w_line[i + 1]]), np.sin([w_line[i], w_line[i + 1]]), color="green", s=30,
                          marker="o")
        axs[0, 0].scatter(np.cos([w_line[i - 1], w_line[i]]), np.sin([w_line[i - 1], w_line[i]]), color="white", s=30,
                          marker="o")

        # top circle
        axs[0, 0].text(x=-1.8, y=1.5, s="Unit Circle")
        axs[0, 0].plot(np.cos([w_line[i], w_line[i + 1]]), np.sin([w_line[i], w_line[i + 1]]), 'green')  # circle
        axs[0, 0].set(xlim=(-2, 2), ylim=(-2, 2))  # circle

        # Ball that traces cosine
        axs[1, 0].scatter([y1_line[i], y1_line[i + 1]], [w_line[i], w_line[i + 1]], color="green", s=30, marker="o")
        axs[1, 0].scatter([y1_line[i - 1], y1_line[i]], [w_line[i - 1], w_line[i]], color="white", s=30, marker="o")

        # cosine wave
        axs[1, 0].text(x=-1.8, y=1, s="Cosine")
        axs[1, 0].plot([y1_line[i], y1_line[i + 1]], [w_line[i], w_line[i + 1]], '#ffd51c')  # cosine

        # ball that traces sine
        axs[0, 1].scatter([w_line[i], w_line[i + 1]], [y2_line[i], y2_line[i + 1]], color="green", s=30, marker="o")
        axs[0, 1].scatter([w_line[i - 1], w_line[i]], [y2_line[i - 1], y2_line[i]], color="white", s=30, marker="o")

        # sine wave
        axs[0, 1].text(x=0.2, y=1.5, s="Sine")
        axs[0, 1].plot([w_line[i], w_line[i + 1]], [y2_line[i], y2_line[i + 1]], '#1c8eff')  # sine
        plt.pause(0.01)

