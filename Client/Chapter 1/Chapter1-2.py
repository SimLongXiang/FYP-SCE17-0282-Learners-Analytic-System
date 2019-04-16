import sys, datetime

try:
    
   
    
except Exception as e:

    #Getting traceback stack information
    exc_type, exc_obj, exc_tb = sys.exc_info()
    
    #Getting System Time
    currentDT = datetime.datetime.now()

    #Error Message Display for Student
    ErrMsg = currentDT.strftime("%H:%M:%S") + "|2| error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1]
    print(ErrMsg)

    #Writing into text file
    with open('/home/pi/Documents/Log Files/PI2.txt', 'a')as f:
        f.write(ErrMsg + "\n")
    

