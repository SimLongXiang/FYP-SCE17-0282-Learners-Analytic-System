import sys, traceback, time, datetime
from sense_hat import SenseHat
sense = SenseHat()

        
try:
    ###------------Insert Code Below------------###
    

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    currentDT = datetime.datetime.now()
    print("error in line" , exc_tb.tb_lineno ,"|", exc_type , "|", exc_obj)
    with open('/home/pi/Documents/Log Files/RPI1.txt', 'a')as f:
        f.write(currentDT.strftime("%H:%M:%S") + "|1|" + str(exc_tb.tb_lineno) + "|" + str(exc_type) + "|" + str(exc_obj) + "\n")
    

