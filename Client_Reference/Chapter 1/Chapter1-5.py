import sys, traceback

import time
from sense_hat import SenseHat
sense = SenseHat()


R = (255, 0, 0)    
G = (0, 255, 0)
B = (0, 0, 255)
Y = (255, 217, 0)
X = (0, 0, 0)

tick = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, G,
    X, X, X, X, X, X, G, G,
    X, X, X, X, X, G, G, X,
    G, X, X, X, G, G, X, X,
    G, G, X, G, G, X, X, X,
    X, G, G, G, X, X, X, X,
    X, X, G, X, X, X, X, X,
]

cross = [
    X, X, X, X, X, X, X, X,
    X, R, R, X, X, R, R, X,
    X, R, R, X, X, R, R, X,
    X, X, X, R, R, X, X, X,
    X, X, X, R, R, X, X, X,
    X, R, R, X, X, R, R, X,
    X, R, R, X, X, R, R, X,
    X, X, X, X, X, X, X, X,
]
try:
    """------------Insert Code Below------------"""
    while True: 
        username = "Nexus"
        password = "1234qwer"

        user = input("Enter username: ")
        pwd = input("Enter password: ")

    ##    if user != username:
    ##        sense.set_pixels(cross)
    ##        print("Wrong username !")
    ##    elif pwd != password:
    ##        sense.set_pixels(cross)
    ##        print("Wrong password !")
        if user != username or pwd != password:
            sense.set_pixels(cross)
            print("Wrong password !")
        
        else:
            sense.set_pixels(tick)
            print("logged in !")
            break

    
   

    """---------------Insert Code Above--------------"""
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    with open('/home/pi/Documents/Log Files/temp.txt', 'w')as f:
        f.write(str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]))
    

