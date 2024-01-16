from matplotlib import pyplot as plt
from scipy.spatial.transform import Rotation as R

#######################################################################################
# How to use this file
#######################################################################################
# This file is a library of functions that can be used to plot data in 3D space.
# To use this file, import it into your own file like this:
# import plot_data
#######################################################################################

#######################################################################################
# What this file does
#######################################################################################
# This file is used to plot data in 3D space using matplotlib in real time.
# It can be used to plot the headset, controllers, base stations, and trackers.
#######################################################################################

#######################################################################################
# Steps in main.py:
#######################################################################################

# 1. Import plot_data_3d.py
# ex:
# import plot_data

# 2. Initialize plot
# ex:
# ax, fig = plot_data.initialize_plot()

# 3. Plot data
# ex:
# list_of_objects = []
# headset_position, headset_rotation = trackerpositions.get_headset_pose()
# list_of_objects.append({"position": headset_position, "rotation": headset_rotation, "color": "k", "name": "headset"})
# plot_data.update_plot(list_of_objects, ax)

# 4. Draw
# ex:
# plot_data.draw(fig)
#
#######################################################################################


#######################################################################################
# Full Example:
#######################################################################################
# import time, openvr
# import trackerpositions
# import plot_data
#
#
# if __name__ == '__main__':
#
#     ax, fig = plot_data.initialize_plot()
#
#     while True:
#
#         list_of_objects = []
#
#         # get headset position and rotation
#         headset_position, headset_rotation = trackerpositions.get_headset_pose()
#         list_of_objects.append({"position": headset_position, "rotation": headset_rotation, "color": "k", "name": "headset"})
#
#         # update plot
#         plot_data.update_plot(list_of_objects, ax)
#
#         # draw
#         plot_data.draw(fig)
#
#         time.sleep(0.1)
#
#######################################################################################

def update_ax(ax):
    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Z', fontsize=14)
    ax.set_zlabel('Y', fontsize=14)
    ax.set_autoscale_on("False")
    # Set limits for each axis
    ax.set_xlim([-8, 8])
    ax.set_ylim([-8, 8])
    ax.set_zlim([-1, 8])
def initialize_plot():
    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    plt.title("3D Space", fontsize=20)
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
        x, y, z = object["position"]
        rotation_matrix = R.from_euler('xyz', object["rotation"], degrees=True).as_matrix()

        # Define axis vectors (assuming they are the columns of the rotation matrix)
        x_axis = rotation_matrix[:, 0]
        y_axis = rotation_matrix[:, 1]
        z_axis = rotation_matrix[:, 2]


        # Plot orientation arrows
        # Red arrow for X-axis
        ax.quiver(x, y, z, x_axis[0], x_axis[1], x_axis[2], color='r', length=1, normalize=True)
        # Green arrow for Y-axis
        ax.quiver(x, y, z, y_axis[0], y_axis[1], y_axis[2], color='g', length=1, normalize=True)
        # Blue arrow for Z-axis
        ax.quiver(x, y, z, z_axis[0], z_axis[1], z_axis[2], color='b', length=1, normalize=True)

        # Plot position
        ax.scatter(x, y, z, marker='o', color=object['color'], zorder=9)

        precision_position = 1
        precision_rotation = 0

        # Plot the text
        text = object["name"]
        # text += f"\nX:{object['position'][0]:.{precision_position}f}"
        # text += f"Y:{object['position'][1]:.{precision_position}f}"
        # text += f"Z:{object['position'][2]:.{precision_position}f}"
        # text += f"P:{object['rotation'][0]:.{precision_rotation}f}°"
        # text += f"R:{object['rotation'][1]:.{precision_rotation}f}°"
        # text += f"Y:{object['rotation'][2]:.{precision_rotation}f}°"

        ax.text(x, y, z, text, fontsize=10, horizontalalignment='center', verticalalignment='bottom',
                color='k', zorder=10)


def draw(fig):
    # update plot
    # drawing updated values
    fig.canvas.draw()

    # This will run the GUI event
    # loop until all UI events
    # currently waiting have been processed
    fig.canvas.flush_events()
