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
 X, X, X, R, R, X, X, X,
 X, X, X, R, R, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X
 ]

two= [
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X,
 X, X, R, R, R, R, X, X,
 X, X, R, X, X, R, X, X,
 X, X, R, X, X, R, X, X,
 X, X, R, R, R, R, X, X,
 X, X, X, X, X, X, X, X,
 X, X, X, X, X, X, X, X
 ]

three= [
 X, X, X, X, X, X, X, X,
 X, R, R, R, R, R, R, X,
 X, R, X, X, X, X, R, X,
 X, R, X, X, X, X, R, X,
 X, R, X, X, X, X, R, X,
 X, R, X, X, X, X, R, X,
 X, R, R, R, R, R, R, X,
 X, X, X, X, X, X, X, X
 ]

four= [
 R, R, R, R, R, R, R, R,
 R, X, X, X, X, X, X, R,
 R, X, X, X, X, X, X, R,
 R, X, X, X, X, X, X, R,
 R, X, X, X, X, X, X, R,
 R, X, X, X, X, X, X, R,
 R, X, X, X, X, X, X, R,
 R, R, R, R, R, R, R, R
 ]

def pattern():
    sense.set_pixels(one)
    time.sleep(0.1)
    sense.set_pixels(two)
    time.sleep(0.1)
    sense.set_pixels(three)
    time.sleep(0.1)
    sense.set_pixels(four)
    time.sleep(0.1)

try:
    """------------Insert Code Below------------"""
    while True:
        pattern()

##    for x in range(0, 5):
##        pattern()
        
        
    

    """---------------Insert Code Above--------------"""
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    with open('/home/pi/Documents/Log Files/temp.txt', 'w')as f:
        f.write(str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]))
    

