from sense_hat import SenseHat
import time, random, logging, sys, os, traceback

logging.basicConfig(level=logging.INFO, format='%(lineno)s , %(msg)s , %(args)s , %(funcName)s, %(module)s')

try:
    sense = SenseHat()

    R = [255, 0, 0]
    B = [0, 0, 255]
    G = [0, 255, 0]

    color_char = [R,B,G]
    PC_choice = []
    human_choice = []
    level = []
    speed = " "


    def level_message(level):
        print("Level: " + str(level) + " Speed: " + str(speed))
        time.sleep(2)

    def flash(color):
        sense.clear(color)
        time.sleep(speed)
        sense.clear()
        time.sleep(speed)

    def converter(color):
        if color == R:
            return "r"
        elif color == B:
            return "b"
        elif color == G:
            return "g"    

    def computer_choice(level):
        PC_choice.clear()
        print("Computer's Turn")
        for i in range(0,level):
            rand_choice = random.choice(color_char)
            PC_choice.append(converter(rand_choice))
            flash(rand_choice)
            print("...")

    def checking(PC, human):
        for i in range(0, level):
            if(PC[i] != human[i]):
                return 0
            else:
                continue
        return 1

    #---------------------Main----------------------------------#

    logging.info("This is a test for logging.")
    print("Welcome to Simon Says!\n")
    time.sleep(1)

    while True: 
        level_message(level)
        computer_choice(level)
        print("Your Turn")
        human_choice = (input("Enter the colors: ")).split(" ")
        answer = checking(PC_choice, human_choice)
        if(answer == 0):
            print("You are wrong !")
            print("Score: " + str(level))
            again = input("Play again? [Y/N]: ")
            if again.lower() == "n":
                print("Thank you for playing !")
                break
            else:
                print("\n")
                continue
        else:
            print("Correct ! Next Level.\n")
            level = level + 1
            speed = speed - 0.05

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("__________________")
    print("Error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    traceback.print_tb(e.__traceback__)
    
    
