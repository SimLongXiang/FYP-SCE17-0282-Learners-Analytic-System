import os
from datetime import datetime
import time

while True:
    os.chdir("/home/pi/Desktop/FYP")
    print("\n")
    print(os.getcwd())

    print("Access Time: " + str(datetime.fromtimestamp(os.stat("Simon_says(Tkinter).py").st_atime)))
    print("Modification Time: " + str(datetime.fromtimestamp(os.stat("Simon_says(Tkinter).py").st_mtime)))
    time.sleep(1)

