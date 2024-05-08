import tkinter as tk
from tkinter import Scale, HORIZONTAL

class FrameSliderApp:
    def __init__(self, root, num_frames, frame_updated_callback, milliseconds_between_frames, export_callback):
        self.root = root
        self.root.title("Frame Slider")

        # Time interval in milliseconds between frame updates
        self.time_between_frames = milliseconds_between_frames

        # Slider for frame selection
        self.slider = Scale(root, from_=0, to=num_frames - 1, orient=HORIZONTAL, command=self.slider_moved)
        self.slider.pack(fill=tk.X, expand=True, padx=10, pady=10)

        # Button to toggle play/pause
        self.playing = False
        self.play_pause_button = tk.Button(root, text="Play", command=self.toggle_play_pause)
        self.play_pause_button.pack(pady=10)

        # Capture Start and End frames
        self.start_frame = 0
        self.end_frame = num_frames - 1

        # Labels to display start and end frames
        self.start_frame_label = tk.Label(root, text=f"Start Frame: {self.start_frame}")
        self.start_frame_label.pack(pady=5)

        self.end_frame_label = tk.Label(root, text=f"End Frame: {self.end_frame}")
        self.end_frame_label.pack(pady=5)

        # Capture Start Button
        self.capture_start_button = tk.Button(root, text="Capture Start", command=self.capture_start)
        self.capture_start_button.pack(pady=5)

        # Capture End Button
        self.capture_end_button = tk.Button(root, text="Capture End", command=self.capture_end)
        self.capture_end_button.pack(pady=5)

        # Export Button
        self.export_button = tk.Button(root, text="Export", command=lambda: export_callback(self.start_frame, self.end_frame))
        self.export_button.pack(pady=5)

        # Callback function to update the frame
        self.frame_updated_callback = frame_updated_callback

        # Setup a method to automatically move the slider
        self.root.after(self.time_between_frames, self.auto_advance)

    def slider_moved(self, value):
        # Convert the slider value to an integer and update frame
        frame_number = int(value)
        self.frame_updated_callback(frame_number)

    def toggle_play_pause(self):
        # Toggle the playing state and update button text
        self.playing = not self.playing
        self.play_pause_button.config(text="Pause" if self.playing else "Play")

    def capture_start(self):
        # Set the start frame to the current slider position and update label
        self.start_frame = self.slider.get()
        self.start_frame_label.config(text=f"Start Frame: {self.start_frame}")
        print(f"Start frame set to: {self.start_frame}")

    def capture_end(self):
        # Set the end frame to the current slider position and update label
        self.end_frame = self.slider.get()
        self.end_frame_label.config(text=f"End Frame: {self.end_frame}")
        print(f"End frame set to: {self.end_frame}")

    def auto_advance(self):
        if self.playing:
            # Advance the slider position if playing
            next_frame = self.slider.get() + 1
            if next_frame <= self.slider['to']:
                self.slider.set(next_frame)
                self.frame_updated_callback(next_frame)
            else:
                # Reset to start or stop at the last frame
                self.slider.set(0)  # Optional: Reset to start
                self.playing = False
                self.play_pause_button.config(text="Play")
        # Schedule the next update
        self.root.after(self.time_between_frames, self.auto_advance)

def frame_updated(frame_number):
    # User implements this function to handle frame updates
    print(f"Displaying frame: {frame_number}")

def export_callback(start_frame, end_frame):
    if start_frame is not None and end_frame is not None:
        print(f"Exporting frames from {start_frame} to {end_frame}")
    else:
        print("Start or end frame not set.")
    # Add here any actions to perform on export like closing the GUI
    # root.destroy()  # Uncomment to close the GUI after exporting

def create_gui(num_frames, milliseconds_between_frames):
    root = tk.Tk()
    app = FrameSliderApp(root, num_frames, frame_updated, milliseconds_between_frames, export_callback)
    root.mainloop()

# Example usage with 100 frames and 500 ms between frames
create_gui(100, 20)
