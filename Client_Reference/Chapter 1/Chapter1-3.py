import sys, traceback

import time
from sense_hat import SenseHat
sense = SenseHat()
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
Y = (255, 217, 0)
X = (0, 0, 0)

one= [
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, B, B, B, B, B, B, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 ]

two = [
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, R, R, R, R, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, R, R, R, R, R, R, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X,
 ]

three = [
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, G, G, G, G, G, G, X,
 X, X, X, X, X, X, X, X,
 X, X, G, G, G, G, X, X,
 X, X, X, X, X, X, X, X,
 X, G, G, G, G, G, G, X,
 X, X, X, X, X, X, X, X,
 ]

four = [
 X, X, X, X, X, X, X, X,
 X, Y, Y, Y, Y, Y, Y, X,
 X, Y, X, Y, Y, X, Y, X,
 X, Y, X, Y, Y, X, Y, X,
 X, Y, Y, X, X, Y, Y, X,
 X, Y, X, X, X, X, Y, X,
 X, Y, Y, Y, Y, Y, Y, X,
 X, X, X, X, X, X, X, X,
 ]

five = [
 X, X, X, X, X, X, X, X,
 X, X, B, B, B, B, X, X,
 X, X, X, B, X, X, X, X,
 X, X, B, B, B, B, X, X,
 X, X, X, B, X, B, X, X,
 X, X, X, B, X, B, X, X,
 X, B, B, B, B, B, B, X,
 X, X, X, X, X, X, X, X,
 ]

def interesting():
    return input("Tell me one interesting thing about you: ")
    
try:
    ###------------Insert Code Below------------###
    print("Hello World")
    Name = input("what is your name? :")
    print("Ah yes, your name is " + Name)
    sense.show_message(Name, scroll_speed = 0.05, back_colour = B, text_colour = R)
    sense.set_pixels(one)
    time.sleep(0.5)
    sense.set_pixels(two)
    time.sleep(0.5)
    sense.set_pixels(three)
    time.sleep(0.5)
    sense.set_pixels(four)
    time.sleep(0.5)
    sense.set_pixels(five)
    time.sleep(0.5)
    
##    sense.clear(red)
##    time.sleep(1)
##    sense.clear(blue)
##    time.sleep(1)
##    sense.clear(green)
    
##    Age = input("How old are you? :")
##    print("wow you are so young at the age of " + Age + " !")
##
##    Age = int(Age) + 5
##    print("You will be " + str(Age) + " in five years time :)")
##
##    Know1 = interesting()
##    Know2 = interesting()
##    Know3 = interesting()
##
##    print("So, 3 interesting thing about you are:\n" + Know1 + "\n" + Know2 + "\n" + Know3)
##    
##    

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    with open('/home/pi/Documents/Log Files/temp.txt', 'w')as f:
        f.write(str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]))
    

