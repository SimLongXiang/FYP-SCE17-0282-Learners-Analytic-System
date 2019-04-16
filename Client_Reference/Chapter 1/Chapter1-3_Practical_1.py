import sys, traceback

import time
from sense_hat import SenseHat
sense = SenseHat()


""" Define colors below (e.g. R = (255, 0, 0)) """
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
Y = (255, 217, 0)
X = (0, 0, 0)

""" Define pattern below (e.g. Diamond = [ shape ]) """
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
 X, X, X, X, X, X, X, X,
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
    
try:
    """------------Define interval Below------------"""
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
    

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    with open('/home/pi/Documents/Log Files/temp.txt', 'w')as f:
        f.write(str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]))
    

