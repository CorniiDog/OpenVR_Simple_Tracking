import time, threading
from toolbox import base_station_control, plot_data_2d, plot_data_3d, trackerpositions
import numpy as np
import json
import tkinter as tk

#######################################################################################
# Setup and Configuration
#######################################################################################

# Display the plot in a window
display_plot = True # Display plot after running (press enter in console to finish recording)
two_dimensional = False # Two-dimensional plot only?
real_time_display = False # Display in real time during recording (Can cause performance issues)

# Enable/disable headset recording
headset = False
headset_name = "Head"

# Enable/disable controller recording
left_controller = True
left_controller_name = "Left Hand"  # "Left Hand"

right_controller = False
right_controller_name = "Right Hand"  # "Right Hand"

# Enable/disable tracker recording
trackers = True
# Tracker Names (Put names for each one that will be present)
tracker_names = ["Right Foot", "Left Foot", "Gun"]

# Enable/disable base station recording
base_stations = False

# Number of base stations to be processed
num_base_stations = 3

# Turn on all known base-stations if possible
turn_on_base_stations = False

# After pressing enter into the console, it would display matplotlib.
# By setting this to false, matplotlib would run automatically
# But setting to true would allow you to press enter to view next frame
press_enter_to_next_frame = False

# Time between position and rotation captures
time_between_captures = 20  # milliseconds between frames (what to aim for)
# Note: Usually frame time is 10 milliseconds above what is put


def update_plot(list_of_objects, ax):
    if two_dimensional:
        # update plot
        plot_data_2d.update_plot(list_of_objects, ax)

        # draw
        plot_data_2d.draw(fig)
    else:
        # update plot
        plot_data_3d.update_plot(list_of_objects, ax)

        # draw
        plot_data_3d.draw(fig)


if __name__ == '__main__':
    def current_milli_time():
        return round(time.time() * 1000)

    if turn_on_base_stations:
        def control_base_stations():
            base_station_control.turn_base_stations_on()
        threading.Thread(target=control_base_stations).start()

    running = True

    ax, fig, plt = None, None, None
    if real_time_display:
        if two_dimensional:
            ax, fig, plt = plot_data_2d.initialize_plot()
        else:
            ax, fig, plt = plot_data_3d.initialize_plot()

    root = None
    # Exit if the user presses x
    def on_exit_func():
        global running
        running = False
        if root is not None:
            root.destroy()


    # Exit if the user presses x
    def listener():
        global root
        root = tk.Tk()
        root.title("Finished Menu")

        button = tk.Button(root, text="Stop Recording", command=on_exit_func)
        button.pack(pady=20, padx=20)

        root.mainloop()

    threading.Thread(target=listener).start()

    history = []
    print("Running")

    while running:

        milli_time = current_milli_time()


        list_of_objects = []

        def update_values(name, pos, rot, color):
            global list_of_objects

            # 1 stud is 0.28 meters, so divide by 0.28 to get the number of studs
            pos = np.array(pos) / 0.28
            # convert to list
            pos = pos.tolist()

            # convert rotation to degrees
            #rot = np.degrees(rot)#np.array(rot) * 180 / np.pi #np.degrees(rot)#np.array(rot) * 180 / np.pi
            # convert to list
            #rot = rot.tolist()

            list_of_objects.append({"position": pos, "rotation": rot, "color": color, "name": name})

        if headset:
            # get headset position and rotation
            headset_position, headset_rotation = trackerpositions.get_headset_pose()
            update_values(headset_name, headset_position, headset_rotation, "k")

        if left_controller:
            # get left controller position and rotation
            left_controller_position, left_controller_rotation = trackerpositions.get_left_controller_pose()
            update_values(left_controller_name, left_controller_position, left_controller_rotation, "r")

        if right_controller:
            # get right controller position and rotation
            right_controller_position, right_controller_rotation = trackerpositions.get_right_controller_pose()
            update_values(right_controller_name, right_controller_position, right_controller_rotation, "b")

        if trackers:
            # get all trackers position and rotation
            for i in range(len(tracker_names)):
                try:
                    if tracker_names[i] == "":
                        continue
                    tracker_position, tracker_rotation = trackerpositions.get_tracker_pose(i)
                    update_values(tracker_names[i], tracker_position, tracker_rotation, "g")
                except:
                    pass

        if base_stations:
            # get all base stations position and rotation
            for i in range(num_base_stations):
                try:
                    base_station_position, base_station_rotation = trackerpositions.get_base_station_pose(i)
                    update_values("Base Station" + str(i), base_station_position, base_station_rotation, "y")
                except:
                    pass

        process_time = current_milli_time() - milli_time

        if real_time_display:
            update_plot(list_of_objects, ax)


        sleep_amount = max(time_between_captures - process_time, 0)
        if sleep_amount > 0:
            time.sleep(sleep_amount/1000)


        history.append([current_milli_time() - milli_time, list_of_objects])

    # Save results as json
    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            return json.JSONEncoder.default(self, obj)

    with open('results.json', 'w') as f:
        json.dump(history, f, cls=NumpyEncoder)

    # Save results as lua file
    indent = "\t"
    with open("results.lua", "w") as export_file:
        export_file.write("data = {\n")

        for item in history:
            list_of_objects = item[1]
            delta_time = item[0]

            export_file.write(indent + " {" + str(delta_time) + ", {\n")

            for object in list_of_objects:
                name = object["name"]
                position = object["position"]
                rotation = object["rotation"]

                export_file.write(f"{indent*2}" + f"[\"{name}\"] = " + "{\n")

                export_file.write(f"{indent * 3}" + f"X = {position[0]}, ")
                export_file.write(f"Y = {position[1]}, ")
                export_file.write(f"Z = {position[2]}, ")
                export_file.write(f"Pitch = {rotation[0]}, ")
                export_file.write(f"Roll = {rotation[1]}, ")
                export_file.write(f"Yaw = {rotation[2]}\n")

                export_file.write(f"{indent * 2}" + "},\n")

            export_file.write(indent + "}},\n")
        export_file.write("}")

    # Initialize plot
    if display_plot:
        print("Playback Started")
        if not ax or not fig or not plt:
            if two_dimensional:
                ax, fig, plt = plot_data_2d.initialize_plot()
            else:
                ax, fig, plt = plot_data_3d.initialize_plot()
            print("Plot initialized")

        # Display the data
        finished = False
        i = 0
        last_frame = len(history) - 1
        time_accumulation = 0
        process_time = 0
        while not finished:

            if i >= last_frame:
                finished = True

            data = history[i]

            list_of_objects = data[1]
            delta_time = data[0]
            i += 1
            time_accumulation += delta_time

            # If process time is lagging behind, skip some frames
            if time_accumulation < process_time:
                continue
            else:
                if press_enter_to_next_frame:
                    if two_dimensional:
                        plot_data_2d.wait_for_button_press()
                    else:
                        plot_data_3d.wait_for_button_press()


            first_time = current_milli_time()

            update_plot(list_of_objects, ax)

            process_time += current_milli_time() - first_time

    plt.close()
