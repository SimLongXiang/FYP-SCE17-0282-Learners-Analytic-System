import mysql.connector as mariadb
import time
from tkinter import *

global level
level = 5
leaderboard = Tk()
connection = mariadb.connect(host='localhost', user='root', db='Highscore')
highest = 0
order = []
temp = 0
temp2 = 0
temp3 = []

def recursive(temp, x):
    global order, temp2
    if x < len(order):
        if temp[1] >= order[x][1]: 
            temp2 = order[x]
            order[x] = temp
            print("end:order(exist lower)" + str(order)+ "\n")
            return recursive(temp2, x+1)
        elif temp[1] < order[x][1]:
            return recursive(temp, x+1)
    else: 
        print("lowest score found" + str(temp))
        return temp

def calculation():
    global order, temp3, highest
    cursor=connection.cursor()
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

    placing.delete(1.0, END)
    
    for x in range (0, len(order)):
        print(order[x])
        placing.insert(INSERT, str(order[x][0]) + "\n")
        placing.tag_add("last", placing.index("end"))
        placing.tag_config("last", justify="right")
        placing.insert(INSERT, str(order[x][1]) + "\n", "last")

    
    order.clear()
    temp3.clear()
    temp = 0
    temp2 = 0


   
#print information
leaderboard.geometry("200x280+300+300")
leaderboard.title("Simons Says")
leaderboard.grab_set()

ld_title = Message(leaderboard, text="Top 10 Leaderboard \n", justify="center", width=200, padx=45)
ld_title.place(x=0, y =10)
ld_frame = LabelFrame(leaderboard, height=200, width=130)
ld_frame.pack(padx=35, pady=30)
ld_frame.pack_propagate(0)
            
placing = Text(ld_frame)
placing.pack()

btn_OK = Button(leaderboard, text="OK", height=2, width=7, command = lambda: calculation())
btn_OK.place(x=60, y=235)



leaderboard.mainloop()
