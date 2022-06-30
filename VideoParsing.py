# Property of Ladar Ltd (https://www.ladar.co.uk/)
# Created by Adan Amjad 29 June 2022

# importing relevant modules
import os
import cv2
import shutil

# setting base directory
parent_directory = 'D:/LadarLtd/Data_Real/M_data'

# accessing folders and sub folder in which the videos aer stored
for folder in os.listdir(parent_directory):
    videoFolder_path = os.path.join(parent_directory, folder)
    print(videoFolder_path)
    for video in os.listdir(videoFolder_path):
        count = -1
        video_path = os.path.join(videoFolder_path, video)
        # making a new directory so store frames of each video separately
        frame_folder = os.path.join(videoFolder_path, video + 'frame')
        os.mkdir(frame_folder)
        os.chdir(frame_folder)
        vid = cv2.VideoCapture(video_path)
        i = -1
        while vid.isOpened():
            ret, frame = vid.read()
            count += 1
            if not ret:
                break
            # modulus will access every 25th frame because we do not want every frame
            if count % 25 == 0:
                i += 1
                # storing frames with specific name and in jpg format
                cv2.imwrite('frame'+str(i)+'.jpg', frame)
        vid.release()
        cv2.destroyAllWindows()
