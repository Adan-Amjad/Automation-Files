# Property of Ladar Ltd (https://www.ladar.co.uk/)
# Created by Adan Amjad 8 June 2022

# importing relevant modules
import os
import shutil

# setting working directory
parent_directory = "D:/LadarLtd/Data"

# setting each class folder as working directory through a loop
# i.e. Jetty, Buoy etc.
# listdir() gives a list of all folders in the specified directory
for classes in os.listdir(parent_directory):
    classes_path = os.path.join(parent_directory, classes)
    count = 0
    # setting each folder in each class as working directory through another loop
    # i.e. 1,2,3..... as many folders as there are
    for every_folder in os.listdir(classes_path):
        # making sure aggregate folder is not confused with other folders
        if every_folder != 'aggregate':
            # setting working directory inside folder 1 through a loop
            folder_path = os.path.join(classes_path, every_folder)
            # this loop will run on each file inside the folder from previous loop
            for file in os.listdir(folder_path):
                # count will keep on assigning new name to the file
                count = count + 1
                # new name is a digit, so it is converted to string
                new_name = str(count) + '.txt'
                # file renamed by defining their paths and names: os.rename(old path, new path)
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
                # moving file from old directory to new directory which is aggregate folder
                move_from = os.path.join(folder_path, new_name)
                move_to = os.path.join(classes_path, "aggregate")
                shutil.move(move_from, move_to)
            # deleting the folder from which files were moved to aggregate folder
            shutil.rmtree(folder_path)

