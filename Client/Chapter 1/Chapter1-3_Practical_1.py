import sys, traceback, time, datetime
from sense_hat import SenseHat
sense = SenseHat()

try:
    ### Define colors below (e.g. R = (255, 0, 0)) ###

    ### Define pattern below (e.g. Diamond = [ shape ]) ###
    
    ###------------Define interval Below------------###
    
    
    
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    currentDT = datetime.datetime.now()
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    with open('/home/pi/Documents/Log Files/temp.txt', 'a')as f:
        f.write(currentDT.strftime("%H:%M:%S") + "|1|" + str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]) + "\n")
    

