# Organizes resources into useful Python data structures


# Imports and includes
import os
import csv


# Constants
RESOURCES_LOCATION = "./resources"


# Returns workout_data, a list of lists including all workout data from all resource files
# Format:  [ [MM.DD.YY, EXERCISE, POUNDS, REPS], [MM.DD.YY, EXERCISE, POUNDS, REPS],... ]
# Example: [ ["10.16.20", "Concentration Curl", "20", "10.8.7"],... ]
def organize_resources():
    # Grab resource file names
    resource_file_names = []
    dir_listing = os.listdir(RESOURCES_LOCATION)
    for item in dir_listing:
        resource_file_names.append(RESOURCES_LOCATION + '/' + item)

    # Process resource files and fill workout_data
    workout_data = []
    for resource_file_name in resource_file_names:
        with open(resource_file_name) as resource_file:
            csv_reader = csv.reader(resource_file, delimiter=',')
            for row in csv_reader:
                if csv_reader.line_num != 1:
                    date = row[0]
                    i = 2
                    while i < len(row):
                        if row[i] != '':
                            workout_data.append([date, row[i], row[i+1], row[i+2]])
                            i = i + 3
                        else:
                            i = i + 1

    # Standardize exercise names
    for workout_datum in workout_data:
        bench_press_aliases = ["chest press", "bench press", "flat barbell chest press", "flat bench"]
        incline_bench_press_aliases = ["incline barbell chest press", "incline bench press", "incline chest press",
                                       "incline bench chest press"]
        overhead_press_aliases = ["over the head press", "overhead barbell press", "overhead press",
                                  "barbell overhead press"]
        bth_overhead_press_aliases = ["behind head overhear press", "behind the head over the head press",
                                      "behind the head overhead press", "behind head overhead press"]
        french_press_aliases = ["french curls", "french press", "overhead barbell french press"]
        if workout_datum[1].lower() in bench_press_aliases:
            workout_datum[1] = "Flat Barbell Bench Press"
        elif workout_datum[1].lower() in incline_bench_press_aliases:
            workout_datum[1] = "Incline Barbell Bench Press"
        elif workout_datum[1].lower() == "incline dumbbell chest press":
            workout_datum[1] = "Incline Dumbbell Bench Press"
        elif workout_datum[1].lower() == "flat dumbbell chest press":
            workout_datum[1] = "Flat Dumbbell Bench Press"
        elif workout_datum[1].lower() in overhead_press_aliases:
            workout_datum[1] = "Overhead Barbell Press"
        elif workout_datum[1].lower() in bth_overhead_press_aliases:
            workout_datum[1] = "BTH Overhead Barbell Press"
        elif workout_datum[1].lower() in french_press_aliases:
            workout_datum[1] = "French Press"

    i = 0
    while i < len(workout_data):
        remove_datum = False
        if workout_data[i][0] == '' or workout_data[i][1] == '':
            remove_datum = True
        for weight in workout_data[i][2].split('.'):
            if not weight.isdigit():
                remove_datum = True
        for rep in workout_data[i][3].split('.'):
            if not rep.isdigit():
                remove_datum = True
        if remove_datum:
            workout_data.remove(workout_data[i])
        else:
            i = i+1

    return workout_data


# Class for organizing workout data
class WorkoutData:
    # Expects to be passed workout_data, formatted as documented by organize_resources()
    def __init__(self, workout_data):
        self.workout_data = workout_data

    # Returns a set of all exercise names contained by this WorkoutData
    def get_exercise_names(self):
        exercise_names = set()
        for workout_datum in self.workout_data:
            exercise_names.add(workout_datum[1])
        return exercise_names

    # Returns a list of lists of all data for the passed exercise name
    def get_exercise_data(self, exercise_name):
        exercise_data = []
        for workout_datum in self.workout_data:
            if workout_datum[1].lower() == exercise_name.lower():
                exercise_data.append(workout_datum)

    # Returns workout_data, formatted as documented by organize_resources()
    def get_workout_data(self):
        return self.workout_data

