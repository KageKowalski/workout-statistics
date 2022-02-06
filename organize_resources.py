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

    return workout_data

