import sys, traceback, time, datetime
from tkinter import *
from sense_hat import SenseHat

try:
    window = Tk()
    sense = SenseHat()

    #Color Definition
    R = [255, 0, 0]
    B = [0, 0, 255]
    G = [0, 255, 0]

    color_char = [R, B, G]
            
    #functions
            
    def flash(color):
        sense.clear(color)
        time.sleep(0.3)
        sense.clear()
        time.sleep(0.3)


    #-------------------------------Frame Widget-------------------------------------------------------#

    window.title("Simon Says")
    window.geometry("460x260")
    window.configure(bg="white")
    output_frame = LabelFrame(window, height=235, width=150, bg="pink")
    output_frame.place(x=295, y=10)


    #------------------------------Display widget-------------------------------------------------------#
    message_frame = LabelFrame(output_frame, height=60, width=130, bg="orange")
    message_frame.place(x=8, y=10)
    message = Label(message_frame, text ="Welcome to Simon Says. Press the Start button to play !", justify="center", fg="white", bg="orange", wraplength=135, anchor="center", width=17)
    message.place(x=0, y =5)

    level_title = Message(output_frame, text="Level: \n", bg="black", fg="white")
    level_title.place(x=0, y =120)
    level_entry = Entry(output_frame, bg="black")
    level_entry.place(x=0, y =170)

    speed_title = Message(output_frame, text="Speed: \n", bg="black", fg="white")
    speed_title.place(x=0, y =140)

    speed_entry = Entry(output_frame, bg="black")
    speed_entry.place(x=0, y =200)

    #---------------------------------Buttons widget---------------------------------------------------#
    #Red Button
    btn_red = Button(window, text="", command=lambda: flash(R), height=7, width=15, bg="green")
    btn_red.place(x=5, y=10)
    #Blue Button


    #Green Button
    btn_green = Button(window, text="Green", command=lambda: flash(G), height=1, width=1, bg="blue")
    btn_green.place(x=75, y=135)
    #Start Button
    btn_start = Button(output_frame, text="", height=2, width=7)
    btn_start.place(x=35, y=80)


    window.mainloop() 

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    currentDT = datetime.datetime.now()
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    with open('/home/pi/Documents/Log Files/temp.txt', 'a')as f:
        f.write(currentDT.strftime("%H:%M:%S") + "|1|" + str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]) + "\n")
    

