# Property of Ladar Ltd (https://www.ladar.co.uk/)
# Created by Adan Amjad 10 June 2022

# # importing relevant modules
import os

# setting working directory
parent_directory = "D:/LadarLtd/DATA"

# class folder will be Jetty, Buoy etc
for classes in os.listdir(parent_directory):
    classes_path = os.path.join(parent_directory, classes)
    # every folder is 1,2,3... folders
    for every_folder in os.listdir(classes_path):
        folder_path = os.path.join(classes_path, every_folder)
        # every file is 001,002,003
        for file in os.listdir(folder_path):
            new_name = classes + "_" + every_folder + "_" + file + ".txt"
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
