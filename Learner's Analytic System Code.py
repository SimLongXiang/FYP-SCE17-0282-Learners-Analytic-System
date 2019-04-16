from tkinter import *
from tkinter import font
import sys, os
from time import sleep

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

TotalError = []
ErrCat = []
CatCount = []
chap1 = []
chap2 = []
chap3 = []
RPI = [1,2,3,4,5,6,7,8,9,10]
start = 0
win = Tk()
win.geometry("1090x570+20+20")
win.title("Class Analysis")
helv14 = font.Font(family='Helvetica', size=14, weight='bold')
helv10 = font.Font(family='Helvetica', size=10, weight='bold')

def log(num):
    ShowLog.delete(1.0, END)
    path = "/home/pi/Documents/Log Files/RPI" + str(num) + ".txt"
    if os.path.exists(path):
        ShowLog.insert(INSERT, "Log Content of RPI " + str(num) + "\n")
        with open(path, "r") as f:
            ShowLog.insert(INSERT, (f.read() + "\n"))
    else:
        ShowLog.insert(INSERT, "Log of RPI " + str(num) + " does not exist !")

def logic(option):
    global TotalError, ShowResult, ShowLog
    TotalError.clear()
    ErrCat.clear()
    CatCount.clear()
    ShowLog.delete(1.0, END)
    ShowResult.delete(0, END)
    
    if option == "0":
        ShowResult.insert(INSERT, "Overall")
        ShowLog.insert(INSERT, "Log Content for Overall:\n")
        for x in range(0,10):
            path = "/home/pi/Documents/Log Files/RPI" + str(x+1) + ".txt"
            if os.path.exists(path):
                with open(path, "r") as f:
                    TotalError.append(0)
                    for lines in f.readlines():
                        info = lines.split("|")
                        TotalError[x] += 1
                        ShowLog.insert(INSERT, lines)
                        piechart(info)
            else:
                TotalError.append(0)
        ShowLog.insert(INSERT, "\nTotal Error Logged: " + str(sum(TotalError)) + "\nBreakdown: " + str(TotalError) )
        
    elif option == "1":
        ShowResult.insert(INSERT, "Chapter 1")
        ShowLog.insert(INSERT, "Log Content for Chapter 1:\n")
        for x in range(0,10):
            path = "/home/pi/Documents/Log Files/RPI" + str(x+1) + ".txt"
            if os.path.exists(path):
                with open(path, "r") as f:
                    TotalError.append(0)
                    for lines in f.readlines():
                        info = lines.split("|")
                        time = int("".join(info[0].split(":")))
                        if time >= 80000 and time <= 140000:
                            TotalError[x] += 1
                            ShowLog.insert(INSERT, lines)
                            piechart(info)
            else:
                TotalError.append(0)
        ShowLog.insert(INSERT, "\nTotal Error Logged: " + str(sum(TotalError)) + "\nBreakdown: " + str(TotalError))
                
    elif option == "2":
        ShowResult.insert(INSERT, "Chapter 2")
        ShowLog.insert(INSERT, "Log Content for Chapter 2:\n")
        for x in range(0,10):
            path = "/home/pi/Documents/Log Files/RPI" + str(x+1) + ".txt"
            if os.path.exists(path):
                with open(path, "r") as f:
                    TotalError.append(0)
                    for lines in f.readlines():
                        info = lines.split("|")
                        time = int("".join(info[0].split(":")))
                        if time > 140000 and time <= 170000:
                            TotalError[x] += 1
                            ShowLog.insert(INSERT, lines)
                            piechart(info)
            else:
                TotalError.append(0)
        ShowLog.insert(INSERT, "\nTotal Error Logged: " + str(sum(TotalError)) + "\nBreakdown: " + str(TotalError))
                            
    elif option == "3":
        ShowResult.insert(INSERT, "Chapter 3")
        ShowLog.insert(INSERT, "Log Content for Chapter 3:\n")
        for x in range(0,10):
            path = "/home/pi/Documents/Log Files/RPI" + str(x+1) + ".txt"
            if os.path.exists(path):
                with open(path, "r") as f:
                    TotalError.append(0)
                    for lines in f.readlines():
                        info = lines.split("|")
                        time = int("".join(info[0].split(":")))
                        if time > 170000:
                            TotalError[x] += 1
                            ShowLog.insert(INSERT, lines)
                            piechart(info)
            else:
                TotalError.append(0)
        ShowLog.insert(INSERT, "\nTotal Error Logged: " + str(sum(TotalError)) + "\nBreakdown: " + str(TotalError) )
                
    elif option == "4":
        chap1.clear()
        chap2.clear()
        chap3.clear()
        logic("1")
        for x in range(len(TotalError)):
            chap1.append(TotalError[x])
        logic("2")
        for x in range(len(TotalError)):
            chap2.append(TotalError[x])
        logic("3")
        for x in range(len(TotalError)):
            chap3.append(TotalError[x])
        logic("0")
        ShowLog.delete(1.0, END)
        ShowResult.delete(0, END)
        ShowResult.insert(INSERT, "Stacked")
        ShowLog.insert(INSERT, "Total Error Logged: " + str(sum(TotalError)))
        ShowLog.insert(INSERT, "\n\nBreakdown\n")
        ShowLog.insert(INSERT, "Chapter 1: " + str(sum(chap1)) + " " + str(chap1))
        ShowLog.insert(INSERT, "\nChapter 2: " + str(sum(chap2)) +  " " + str(chap2))
        ShowLog.insert(INSERT, "\nChapter 3: " + str(sum(chap3)) +  " " + str(chap3))
        ShowLog.insert(INSERT, "\n\nUse Result Options to see in-depth chapter analysis.")
        
    elif option == "5":
        if int(ST.get()) >= 0 and int(ST.get()) <= 235959 and int(ET.get()) >= 0 and int(ET.get()) <= 235959 and int(ST.get()) < int(ET.get()):
            ShowResult.insert(INSERT, ST.get() + " to " + ET.get())
            ShowLog.insert(INSERT, "Log Content between " + ST.get() + " to " + ET.get() + "\n")
            for x in range(0,10):
                path = "/home/pi/Documents/Log Files/RPI" + str(x+1) + ".txt"
                if os.path.exists(path):
                    with open(path, "r") as f:
                        TotalError.append(0)
                        for lines in f.readlines():
                            info = lines.split("|")
                            time = int("".join(info[0].split(":")))
                            if time >= int(ST.get()) and time <= int(ET.get()):
                                TotalError[x] += 1
                                ShowLog.insert(INSERT, lines)
                                piechart(info)
                else:
                    TotalError.append(0)
            ShowLog.insert(INSERT, "\nTotal Error Logged: " + str(sum(TotalError)) + "\nBreakdown: " + str(TotalError) )
                    
        elif ST.get() == "" or ET.get() == "":
            messagebox.showwarning("No Valid Values","Please Enter Value !")
        else:
            messagebox.showwarning("Invalid Values","Invalid Values !\nEnter time in 24hr format !")
    

    refreshgraph(option)

def piechart(info):
    if info[3] in ErrCat:
        pos = ErrCat.index(info[3])
        CatCount[pos] += 1
    else:
        ErrCat.append(info[3])
        CatCount.append(1)

def refreshgraph(option):
    global chap1, chap2, chap3
    if start > 0:
        a.clear()
        b.clear()
        
        if option == "4":
            S1 = a.bar(RPI,chap1, color="grey", align="center", width=0.50)
            S2 = a.bar(RPI,chap2, bottom=chap1, color="yellow", align="center", width=0.50)
            S3 = a.bar(RPI,chap3, bottom=list(map(lambda x,y:x+y, chap1,chap2)), color="red", align="center", width=0.50)
            a.set_ylabel("Total No. of Errors Made")
            a.set_xticks(RPI)
            a.grid(axis='y')
            a.legend((S1[0], S2[0], S3[0]),('Chapter1','Chapter2', 'Chapter3'), fontsize=10, loc='best')
        else:
            a.bar(RPI,TotalError, align="center", width=0.50)
            a.set_ylabel("Total No. of Errors Made")
            a.set_xticks(RPI)
            a.grid(axis='y')
             
        b.pie(CatCount, labels=ErrCat, autopct='%1.1f%%', shadow=True, startangle=90)
        b.axis('equal')
        f.canvas.draw()
        f2.canvas.draw()

""" Titles & Headers """
Label(win, text="Error Progress", font=helv14).place(x=175,y=7)
Label(win, text="Log Content", font=helv14).place(x=725,y=325)
Label(win, text="Error Category", font=helv14).place(x=725,y=7)
Label(win, text="Showing result from: ", font=helv14).place(x=25,y=350)

""" Text Widgets """
ShowResult = Entry(win, bg = "black", fg = "lightgreen", width = 25, justify = "center")
ShowResult.place(x=260, y=354)
ShowLog = Text(win, bg = "black", fg="white", height = 10, width = 83)
ShowLog.place(x=490, y=350)

""" Buttons """
RF = Button(win, text="Refresh", height=2, width=8, command = lambda: logic("0"))
RF.place(x=120, y=500)
EX = Button(win, text="Exit", height=2, width=8, command = lambda: os._exit(0))
EX.place(x=240, y=500)

RPIFrame = LabelFrame(win, text="Participant's RPI")
RPIFrame.place(x=490, y=505)
RPI1 = Button(RPIFrame, text="RPI1", height=1, width=3, command = lambda: log(1))
RPI1.grid(column=0, row=0, padx = (3,3), pady = (3,3))
RPI2 = Button(RPIFrame, text="RPI2", height=1, width=3, command = lambda: log(2))
RPI2.grid(column=1, row=0, padx = (3,3), pady = (3,3))
RPI3 = Button(RPIFrame, text="RPI3", height=1, width=3, command = lambda: log(3))
RPI3.grid(column=2, row=0, padx = (3,3), pady = (3,3))
RPI4 = Button(RPIFrame, text="RPI4", height=1, width=3, command = lambda: log(4))
RPI4.grid(column=3, row=0, padx = (3,3), pady = (3,3))
RPI5 = Button(RPIFrame, text="RPI5", height=1, width=3, command = lambda: log(5))
RPI5.grid(column=4, row=0, padx = (3,3), pady = (3,3))
RPI6 = Button(RPIFrame, text="RPI6", height=1, width=3, command = lambda: log(6))
RPI6.grid(column=5, row=0, padx = (3,3), pady = (3,3))
RPI7 = Button(RPIFrame, text="RPI7", height=1, width=3, command = lambda: log(7))
RPI7.grid(column=6, row=0, padx = (3,3), pady = (3,3))
RPI8 = Button(RPIFrame, text="RPI8", height=1, width=3, command = lambda: log(8))
RPI8.grid(column=7, row=0, padx = (3,3), pady = (3,3))
RPI9 = Button(RPIFrame, text="RPI9", height=1, width=3, command = lambda: log(9))
RPI9.grid(column=8, row=0, padx = (3,3), pady = (3,3))
RPI10 = Button(RPIFrame, text="RPI10", height=1, width=3, command = lambda: log(10))
RPI10.grid(column=9, row=0, padx = (0,3), pady = (3,3))

""" Result options """
RO = LabelFrame(win, text="Results Option")
RO.place(x=25, y=375)
C1 = Button(RO, text="chapter 1", height=2, width=6, command = lambda: logic("1"))
C1.grid(padx=5, pady=5)
C2 = Button(RO, text="chapter 2", height=2, width=6, command = lambda: logic("2"))
C2.grid(column=1,row=0, padx=5, pady=5)
C3 = Button(RO, text="chapter 3", height=2, width=6, command = lambda: logic("3"))
C3.grid(column=2,row=0, padx=5, pady=5)
C4 = Button(RO, text="Overall", height=2, width=6, command = lambda: logic("0"))
C4.grid(column=3,row=0, padx=5, pady=5)
C5 = Button(RO, text="Stacked", height=2, width=6, command = lambda: logic("4"))
C5.grid(column=4,row=0, padx=5, pady=5)

Label(RO, text="Start Time:", font=helv10).grid(column=1,row=1)
Label(RO, text="End Time: ", font=helv10).grid(column=1,row=2)

ST = Entry(RO, width = 10)
ST.grid(column=2, row=1)
ET = Entry(RO, width = 10)
ET.grid(column=2, row=2)

GO = Button(RO, text="GO !", height=2, width=6, command = lambda: logic("5"))
GO.grid(rowspan=2, column=3, row=1)

logic("0")

""" Initial Graphs """
f = Figure(figsize=(6,3.5), dpi=80)
a = f.add_subplot(111)
a.bar(RPI,TotalError, align="center", width=0.50)
a.set_ylabel("Total No. of Errors Made")
a.set_xticks(RPI)
a.grid(axis='y')
canvas = FigureCanvasTkAgg(f, win)
canvas.show()
canvas.get_tk_widget().place(x=10, y=35)

f2 = Figure(figsize=(7,3.5), dpi=80)
b = f2.add_subplot(111)
b.pie(CatCount, labels=ErrCat, autopct='%1.1f%%', shadow=True, startangle=90)
b.axis('equal')
canvas2 = FigureCanvasTkAgg(f2, win)
canvas2.show()
canvas2.get_tk_widget().place(x=510, y=35)

start += 1

win.mainloop()


