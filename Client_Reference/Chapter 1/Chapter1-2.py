import sys, traceback

try:
    ###------------Insert Code Below------------###
    print("Hello World")
    Name = input("what is your name? :")
    print("Ah yes, your name is " + Name)
    Age = input("How old are you? :")
    print("wow you are so young at the age of " + Age + " !")

    Age = int(Age) + 5.4
    print("You will be " + str(Age) + " in five years time :)")

    Know1 = input("Tell me one interesting thing about you :")
    Know2 = input("Another one :")
    Know3 = input("Last one :")

    print("So, 3 interesting thing about you are:\n" + Know1 + "\n" + Know2 + "\n" + Know3)
    
    

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    with open('/home/pi/Documents/Log Files/temp.txt', 'w')as f:
        f.write(str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]))
    

