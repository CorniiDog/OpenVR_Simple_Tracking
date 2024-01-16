from matplotlib import pyplot as plt
from scipy.spatial.transform import Rotation as R
def update_ax(ax):
    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Z', fontsize=14)
    ax.set_autoscale_on("False")
    # Set limits for each axis
    ax.set_xlim([-8, 8])
    ax.set_ylim([-8, 8])

def initialize_plot():
    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111)  # 2D plot

    plt.title("2D Top-Down View", fontsize=20)
    plt.show()
    return ax, fig

def wait_for_button_press():
    a = plt.waitforbuttonpress()
    if not a:
        wait_for_button_press()

def update_plot(list_of_objects, ax):
    ax.clear()
    update_ax(ax)

    for object in list_of_objects:
        x, y, _ = object["position"]

        rotation_matrix = R.from_euler('xyz', object["rotation"], degrees=True).as_matrix()
        z_axis = -rotation_matrix[:, 2]

        # Plot position
        ax.scatter(x, y, marker='o', color=object["color"])

        # Plot orientation arrow
        ax.quiver(x, y, z_axis[0], z_axis[1], color=object["color"], scale=1, scale_units='xy', angles='xy')

        # Plot the text
        ax.text(x, y, object["name"], fontsize=10, horizontalalignment='center', verticalalignment='bottom', color='k',
                zorder=1)

def draw(fig):
    # update plot
    # drawing updated values
    fig.canvas.draw()

    # This will run the GUI event
    # loop until all UI events
    # currently waiting have been processed
    fig.canvas.flush_events()