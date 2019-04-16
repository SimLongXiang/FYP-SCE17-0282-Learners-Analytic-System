from tkinter import *
from sense_hat import SenseHat
import time

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
window.configure(bg="black")
output_frame = LabelFrame(window, text="menu", height=235, width=150, bg="black")
output_frame.place(x=295, y=10)


#------------------------------Display widget-------------------------------------------------------#
message_frame = LabelFrame(output_frame, height=60, width=130, bg="black")
message_frame.place(x=8, y=10)
message = Label(message_frame, text ="Welcome to Simon Says. Press the Start button to play !", font=("arial", 8), justify="center", fg="white", bg="black", wraplength=130, width=17)
message.place(x=0, y =5)

level_title = Message(output_frame, text="Level: \n", bg="black", fg="white")
level_title.place(x=0, y =80)
level_entry = Entry(output_frame, bg="black", width=15)
level_entry.place(x=5, y =100)

speed_title = Message(output_frame, text="Speed: \n", bg="black", fg="white")
speed_title.place(x=0, y =120)
speed_entry = Entry(output_frame, bg="black", width=15)
speed_entry.place(x=5, y =140)

#---------------------------------Buttons widget---------------------------------------------------#
buttons = []
#Red Button
btn_red = Button(window, text="Red", command=lambda: flash(R), height=7, width=15, bg="red")
btn_red.place(x=5, y=10)
#Blue Button
btn_blue = Button(window, text="Blue", command=lambda: flash(B), height=7, width=15, bg="blue")
btn_blue.place(x=145, y=10)
#Green Button
btn_green = Button(window, text="Green", command=lambda: flash(G), height=7, width=15, bg="green")
btn_green.place(x=75, y=135)
#Start Button
btn_start = Button(output_frame, text="Start!", height=2, width=7, bg="black", fg="white")
btn_start.place(x=35, y=170)
buttons.append(btn_start)


window.mainloop() 
