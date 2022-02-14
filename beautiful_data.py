# Displays organized workout data in a beautiful way


# Imports
import tkinter as tk
from ScrollFrame import ScrollFrame
from organize_resources import WorkoutData
from organize_resources import organize_resources


# Global variables
workout_data = WorkoutData(organize_resources())
gui = tk.Tk()


# Configure GUI
def configure_gui():
    gui.title("beautiful_data")
    gui.geometry("1920x1080")

    # Configure button frame
    button_frame = ScrollFrame(gui)
    button_frame.pack(side=tk.LEFT, fill=tk.Y)

    exercise_names = workout_data.get_exercise_names()
    for exercise_name in exercise_names:
        button = tk.Button(button_frame.viewPort, text=exercise_name, width=30)
        button.pack()


# Loop the GUI
configure_gui()
gui.mainloop()

