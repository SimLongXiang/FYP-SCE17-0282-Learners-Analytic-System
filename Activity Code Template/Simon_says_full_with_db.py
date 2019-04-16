from tkinter import *
import mysql.connector as mariadb
from sense_hat import SenseHat
from threading import Thread
import time
import random

window = Tk()
sense = SenseHat()
dbconnect = mariadb.connect(host='localhost', user='root', db='Highscore')
cursor = dbconnect.cursor()

#Variables
PC_choice = []
human_choice = []
level = 1
speed = 0.5
sflag = 0

#Color Definition
R = [255, 0, 0]
B = [0, 0, 255]
G = [0, 255, 0]
O = [0, 0, 0]

tick = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, G, O,
O, O, O, O, O, G, O, O,
O, O, O, O, G, O, O, O,
O, G, O, G, O, O, O, O,
O, O, G, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

cross = [
O, O, O, O, O, O, O, O,
O, R, O, O, O, O, R, O,
O, O, R, O, O, R, O, O,
O, O, O, R, R, O, O, O,
O, O, O, R, R, O, O, O,
O, O, R, O, O, R, O, O,
O, R, O, O, O, O, R, O,
O, O, O, O, O, O, O, O
]

color_char = [R, B, G]
        
#--------------------------------functions-----------------------------------------#
def insertion(user,toplevel):
    global level, speed, cursor
    
    cursor.execute('insert into scores VALUES ("%s", "%s")' % (user, level))
    dbconnect.commit()
    print("values inserted...")
    toplevel.destroy()
    level = 1
    speed = 0.5
    scores()

    
##    dbconnect.close()

def scores():
    global cursor
    
    cursor.execute("select * from scores order by score desc limit 14")
    data=cursor.fetchall()
    print("values retrieved...")
    
    n_placing.delete(0, END)
    s_placing.delete(0, END)
    for x in range (0, len(data)):
        n_placing.insert(END, data[x][0])
        s_placing.insert(END, str(data[x][1]))
    print("values placed...")
    
def flashcorrect(diagram):
    for x in range(0,2):
        sense.set_pixels(diagram)
        time.sleep(0.3)
        sense.clear()
        time.sleep(0.3)
        
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
    human_choice.clear()

    sense.clear()
    message_show.set("Computer's Turn")
    time.sleep(1)
    
    for i in range(0,level):
        rand_choice = random.choice(color_char)
        PC_choice.append(converter(rand_choice))
        flash(rand_choice)
        
    global human_count
    human_count = len(PC_choice)

    for i in range(0,3):
        buttons[i].config(state = NORMAL)
    message_show.set("Your Turn !\nPress the color in correct order !")

def player_choice(color):
    global human_count
    
    if(human_count != 0):
        human_choice.append(converter(color))
        human_count -= 1

        if(human_count == 0):
            checking(PC_choice, human_choice)
            
        
def checking(PC, human):
    global level
    global speed
    global correctness
    correctness = 1

    #check if color matches bet. player and computer
    for i in range(0, level):
        if(PC[i] != human[i]):
            correctness = 0  

    if correctness == 1:
        level += 1
        speed = round((speed - 0.05), 2)
        
        message_show.set("Correct ! Next Level !")
        flashcorrect(tick)

        if speed < 0.25:
            speed = 0.25

        level_show.set(level)
        speed_show.set(speed)
        start_game()

    else:
        message_show.set("Wrong !\nFinal score: " + str(level) + "\nTry again !")
        flashcorrect(cross)
        highscore()
        buttons[3].config(state = NORMAL)
        
def start_game():
    global sflag
    
    level_show.set(level)
    speed_show.set(speed)
    for i in range(0,4):
        buttons[i].config(state = DISABLED)
    sflag = 1
    sense.show_message("Ready?", scroll_speed=0.03)

def start_flag():
    global sflag
    
    while True:
        if(sflag == 1):
            computer_choice(level)
            sflag = 0
    
t = Thread(target=start_flag)
t.start()
#-------------------------------Top level Widget---------------------------------------------------#
def highscore():
    highscores = Toplevel(window)
    highscores.geometry("200x110+50+50")
    highscores.grab_set()
    
    name_title = Message(highscores, text="Enter your name: \n", justify="center", width=200, padx=25)
    name_title.place(x=0, y =10)
    name_entry = Entry(highscores)
    name_entry.place(x=20, y =30)

    btn_OK = Button(highscores, text="OK", height=2, width=7, command = lambda: insertion(name_entry.get(),highscores))
    btn_OK.place(x=55, y=55)
    
    

#-------------------------------Frame Widget-------------------------------------------------------#
window.title("Simon Says")
window.geometry("400x260+50+50")
window.configure(bg="black")

ld_title = Message(window, text="High Score", width=70, bg="black", fg="white")
ld_title.place(x=22,y=12)
n_placing = Listbox(window, height=14, width=9, bg="black", fg="white")
n_placing.grid(rowspan=3, padx=(4,0), pady=(10,0))
s_placing = Listbox(window, height=14, width=3, bg="black", fg="white")
s_placing.grid(column=1, row=0, rowspan=3, padx=(2,0), pady=(10,0))
#---------------------------------Buttons widget---------------------------------------------------#
buttons = []

#Green Button
btn_green = Button(window, text="Green", command=lambda: player_choice(G), height=3, width=9, bg="green", fg="black", state= DISABLED)
btn_green.grid(column=2, row=0, pady=(5,0), padx=(10,0))
buttons.append(btn_green)
#Red Button
btn_red = Button(window, text="Red", command=lambda: player_choice(R), height=3, width=9, bg="red", fg="black", state= DISABLED)
btn_red.grid(column=2, row=1, pady=(3,0), padx=(10,0))
buttons.append(btn_red)
#Blue Button
btn_blue = Button(window, text="Blue", command=lambda: player_choice(B), height=3, width=9, bg="blue", fg="black", state= DISABLED)
btn_blue.grid(column=2, row=2, pady=(3,0), padx=(10,0))
buttons.append(btn_blue)

#------------------------------Display widget-------------------------------------------------------#
output_frame = LabelFrame(window, height=235, width=150, bg="black")
output_frame.grid(column=3, row=0, rowspan=3, padx=10, pady=15)

message_frame = LabelFrame(output_frame, height=60, width=130, bg="black")
message_frame.place(x=8, y=10)
message_show = StringVar()
message = Label(message_frame, textvariable= message_show, justify="center", fg="white", bg="black", wraplength=135, anchor="center", width=15)
message_show.set("Welcome to Simon Says. Press Start to play !")
message.place(x=0, y =5)

level_title = Message(output_frame, text="Level: \n", bg="black", fg="white")
level_title.place(x=0, y =80)
level_show = StringVar()
level_entry = Entry(output_frame, textvariable=level_show, state = "readonly", bg="black")
level_entry.place(x=0, y =100)

speed_title = Message(output_frame, text="Speed: \n", bg="black", fg="white")
speed_title.place(x=0, y =120)
speed_show = StringVar()
speed_entry = Entry(output_frame, textvariable=speed_show, state = "readonly", bg="black")
speed_entry.place(x=0, y =140)

#Start Button
btn_start = Button(output_frame, text="Start!", height=2, width=7, command = lambda: start_game(), bg="black", fg="white")
btn_start.place(x=32, y=180)
buttons.append(btn_start)

window.mainloop() 
