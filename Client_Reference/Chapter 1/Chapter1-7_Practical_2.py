import sys, traceback

import time
from sense_hat import SenseHat
sense = SenseHat()

R = (255, 0, 0)
B = (0, 0, 255)
X = (0, 0, 0)
O = (255, 116, 21)


face1 = [
    X, X, X, X, X, X, X, X,
    O, O, O, X, X, O, O, O,
    O, X, O, X, X, O, X, O,
    O, O, O, X, X, O, O, O,
    X, X, X, X, X, X, X, X,
    X, O, X, X, X, X, O, X,
    X, O, X, X, X, X, O, X,
    X, X, O, O, O, O, X, X
]

face2 = [
    X, X, X, X, X, X, X, X,
    X, O, X, X, X, X, O, X,
    O, O, O, X, X, O, O, O,
    X, O, X, X, X, X, O, X,
    X, X, X, X, X, X, X, X,
    X, O, O, O, O, O, O, X,
    X, O, X, X, X, X, O, X,
    X, X, O, O, O, O, X, X
]
try:
    """------------Insert Code Below------------"""
    while True:
        Name = input("Hi, what is your name? :")
        Gender = input("Are you a male or female? (M/F):")
        if Gender == "M":
            print("Hi there, " + Name + ". You are one good-looking male!")
            sense.show_message(Name, text_colour=B)
        elif Gender == "F":
            print("Hi there, " + Name + ". You are beautiful!")
            sense.show_message(Name, text_colour=R)
        else:
            print("I think you have entered wrongly ! just enter F or M !")
            sense.show_message("???")
            break
        print("My Name is Long Xiang !")
        sense.show_message("Long Xiang", text_colour=B)
        print("This is my animation")
        time.sleep(1)
        
        for x in range(0,6):
            sense.set_pixels(face1)
            time.sleep(0.25)
            sense.set_pixels(face2)
            time.sleep(0.25)

        print("Thank you ! Next user please.")
   

    """---------------Insert Code Above----------"""
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    with open('/home/pi/Documents/Log Files/temp.txt', 'w')as f:
        f.write(str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]))
    

