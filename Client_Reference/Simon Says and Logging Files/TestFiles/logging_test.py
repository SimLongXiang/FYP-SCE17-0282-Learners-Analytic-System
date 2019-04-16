import sys, os, traceback, logging
#logging.basicConfig(level=logging.INFO, format='%(lineno)s , %(msg)s , %(args)s , %(funcName)s, %(module)s')

try:

    def add(a,b):
        return 

    print(add(2,a))
    

except Exception as e:
##    print(traceback.format_exc())
    print("____1_____")
##    print(sys.exc_info()[0])
##    print(sys.exc_info()[1])
##    print(sys.exc_info()[2])
##    print("____2_____")
##    
##    logging.exception(str(e))
##    print("____3_____")
##    traceback.print_tb(e.__traceback__)
##    print("____4_____")
##    traceback.print_exc()
##    print("____5_____")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
##    print(exc_type, fname, exc_tb.tb_lineno)
##    print("____6_____")
##    print(exc_tb.tb_frame, exc_tb.tb_lineno)
##    print("____7_____")
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])

    with open('text.txt', 'w')as f:
        f.write(str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]))
    

