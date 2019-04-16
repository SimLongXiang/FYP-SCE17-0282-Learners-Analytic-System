from tkinter import *
import mysql.connector as mariadb
from sense_hat import SenseHat
from threading import Thread
import time
import random

window = Tk()
sense = SenseHat()

#Variables
PC_choice = []
human_choice = []
level = 1
speed = 0.5
sflag = 0

highest = 0
order = []
temp = 0
temp2 = 0
temp3 = []

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
    global level, speed
    
    #insert info
    dbconnect = mariadb.connect(host='localhost', user='root', db='Highscore')
    cursor = dbconnect.cursor()
    cursor.execute('insert into scores VALUES ("%s", "%s")' % (user, level))
    dbconnect.commit()
    print("values inserted...")
    toplevel.destroy()
    level = 1
    speed = 0.5
    leaderboard()
    
        
def flashcorrect(diagram):
    sense.set_pixels(diagram)
    time.sleep(0.3)
    sense.clear()

        
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

    for i in range(1,4):
        buttons[i].config(state = NORMAL)
    message_show.set("Your Turn !\nPress the color in correct order !")

def player_choice(color):
    global human_count
    
    if(human_count != 0):
        #flash(color)
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
        level_show.set(level)
        speed_show.set(speed)
        message_show.set("Correct ! Next Level !")
        flashcorrect(tick)
        start_game()

    else:
        message_show.set("Wrong !\nFinal score: " + str(level) + "\nTry again !")
        flashcorrect(cross)
        highscore()
        buttons[0].config(state = NORMAL)
        
def start_game():
    global sflag
    
    level_show.set(level)
    speed_show.set(speed)
    for i in range(0,4):
        buttons[i].config(state = DISABLED)
    sflag = 1

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
    btn_OK.place(x=5, y=55)
    btn_cancel = Button(highscores, text="Cancel", height=2, width=7, command = lambda: highscores.destroy())
    btn_cancel.place(x=105, y=55)

def leaderboard():
    global highest, temp3, order
    highest = 0
    temp3.clear()
    order.clear()
    leaderboard = Toplevel(window) 
    leaderboard.geometry("200x280+100+50")
    leaderboard.grab_set()

    ld_title = Message(leaderboard, text="Top 10 Leaderboard \n", justify="center", width=200, padx=45)
    ld_title.place(x=0, y =10)
    ld_frame = LabelFrame(leaderboard, height=200, width=130)
    ld_frame.pack(padx=35, pady=30)
    ld_frame.pack_propagate(0)

    dbconnect = mariadb.connect(host='localhost', user='root', db='Highscore')
    cursor = dbconnect.cursor()
    cursor.execute("select * from scores")
    data=cursor.fetchall()
    
    for row in data:
        print("start:row " + str(row))
        print("start:order " + str(order))
        if row[1] > highest:                                        # check if breaks highscore
            highest = row[1]
            print("highest: " + str(highest))
            if order == []:                                         # check if order is empty
                order.append(row)
                print("end:order(list empty)" + str(order) + "\n")
            else:                                                   # there exist a previous highscore
                temp3.append(row)                                   # put current highscore in temp. list
                for x in range(0,len(order)):                       # replace into temp. list                 
                    temp3.append(order[x])
                order.append(0)                                     # add one to original order list
                for x in range(0, len(temp3)):
                    order[x] = temp3[x]                             # move back to original list
                print("end:order(exist previous highscore)" + str(order)+ "\n")
        else:                                                       # not a highscore
            lowest = recursive(row, 0)
            order.append(lowest)                                    #  lowest score
            print("end:(lowest score) " + str(order) + "\n")

    placing = Text(ld_frame)
    placing.pack()
    for x in range (0, len(order)):
        print(order[x])
        placing.insert(INSERT, str(order[x][0]) + "\n")
        placing.tag_add("last", placing.index("end"))
        placing.tag_config("last", justify="right")
        placing.insert(INSERT, str(order[x][1]) + "\n", "last")
    
    btn_OK = Button(leaderboard, text="OK", height=2, width=7, command = lambda: leaderboard.destroy())
    btn_OK.place(x=60, y=235)
    dbconnect.close()

def recursive(temp, x):
    global order, temp2
    if x < len(order):
        if temp[1] >= order[x][1]: 
            temp2 = order[x]
            order[x] = temp
            print("end:order(exist lower)" + str(order))
            return recursive(temp2, x+1)
        elif temp[1] < order[x][1]:
            return recursive(temp, x+1)
    else: 
        print("lowest score found" + str(temp))
        return temp
#-------------------------------Frame Widget-------------------------------------------------------#

window.title("Simon Says")
window.geometry("460x260+50+50")
window.configure(bg="black")
output_frame = LabelFrame(window, height=235, width=150, bg="black")
output_frame.place(x=295, y=10)
#------------------------------Display widget-------------------------------------------------------#
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

#---------------------------------Buttons widget---------------------------------------------------#
buttons = []
#Start Button
btn_start = Button(output_frame, text="Start!", height=2, width=7, command = lambda: start_game(), bg="black", fg="white")
btn_start.place(x=35, y=180)
buttons.append(btn_start)
#Red Button
btn_red = Button(window, text="Red", command=lambda: player_choice(R), height=5, width=12, bg="red", fg="black", state= DISABLED)
btn_red.place(x=20, y=40)
buttons.append(btn_red)
#Green Button
btn_green = Button(window, text="Green", command=lambda: player_choice(G), height=5, width=12, bg="green", fg="black", state= DISABLED)
btn_green.place(x=90, y=135)
buttons.append(btn_green)
#Blue Button
btn_blue = Button(window, text="Blue", command=lambda: player_choice(B), height=5, width=12, bg="blue", fg="black", state= DISABLED)
btn_blue.place(x=160, y=40)
buttons.append(btn_blue)




window.mainloop() 
