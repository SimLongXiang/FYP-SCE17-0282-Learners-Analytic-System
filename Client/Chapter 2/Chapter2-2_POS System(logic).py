import sys, traceback, time, datetime
from tkinter import *
    
try:
    POS = Tk()
    ###--------CREATE FUNCTION CODE BELOW--------###
    

    
     
    ###-----FIND BUTTONS TO CALL FUNCTION----####
    POS.title("Nexus Cafe POS system")
    POS.geometry("700x380+50+50")

    Label(POS, text="Cafe Menu", font=("Helvetica", 18)).place(x=120, y=1)
    Label(POS, text="Food Order", font=("Helvetica", 18)).place(x=480, y=1)

    SB = LabelFrame(POS, text="Small Bites", height=100, width=300, bg="yellow")
    SB.place(x=15, y=30)
    TF = Button(SB, text="Truffles Fries\nS$5", height=3, width=12)
    TF.grid(padx=5, pady=5)
    CW = Button(SB, text="Chicken Wings\nS$7", height=3, width=12)
    CW.grid(column=1,row=0, padx=5, pady=5)
    CL = Button(SB, text="Calamari\nS$5", height=3, width=12)
    CL.grid(column=2,row=0, padx=5, pady=5)

    SB = LabelFrame(POS, text="Mains", height=100, width=300, bg="blue")
    SB.place(x=15, y=120)
    TF = Button(SB, text="Salted Egg Prawn Pasta\nS$13", height=3, width=12, wraplength=80)
    TF.grid(padx=5, pady=5)
    CW = Button(SB, text="Aglio Olio\nS$6.50", height=3, width=12)
    CW.grid(column=1,row=0, padx=5, pady=5)
    CL = Button(SB, text="Carbonara\nS$8", height=3, width=12, wraplength=80)
    CL.grid(column=2,row=0, padx=5, pady=5)
    P = Button(SB, text="Sirloin Steak\nS$17", height=3, width=12)
    P.grid(row=1, padx=5, pady=5)
    MS = Button(SB, text="Black Pepper Chicken Chop\nS$12", height=3, width=12, wraplength=100)
    MS.grid(column=1,row=1, padx=5, pady=5)
    GB = Button(SB, text="Grilled Salmon\nS$14", height=3, width=12)
    GB.grid(column=2,row=1, padx=5, pady=5)

    SB = LabelFrame(POS, text="Drinks and Dessert", bg="green")
    SB.place(x=15, y=280)
    TF = Button(SB, text="Ice Cream Waffles\nS$7", height=3, width=12, wraplength=80)
    TF.grid(padx=5, pady=5)
    CW = Button(SB, text="Coke/Sprite/Root Beer Float\nS$3", height=3, width=12, wraplength=110)
    CW.grid(column=1,row=0, padx=5, pady=5)
    CL = Button(SB, text="Canned Drinks\nS$1.50", height=3, width=12, wraplength=100)
    CL.grid(column=2,row=0, padx=5, pady=5)

    Submit = Button(POS, text="Submit", height=2, width=6)
    Submit.place(x=430, y=270)
    Clear = Button(POS, text="Clear", height=2, width=6,command=lambda: clearlist())
    Clear.place(x=430, y=320)
    

    ShowOrder = Text(POS, height=16, width = 30, bg="black", foreground="red")
    ShowOrder.place(x=430, y=35)
    ShowPrice = Text(POS, height=16, width = 5, bg="black", foreground="red")
    ShowPrice.place(x=650, y=35)
    
    Label(POS, text="Sub-total:").place(x=540, y=280)
    Label(POS, text="GST (7%):").place(x=540, y=305)
    Label(POS, text="Grand-total:").place(x=525, y=330)
    ST = Label(POS, height=1, width = 10, bg="black", foreground="white")
    ST.place(x=605, y=280)
    GST = Label(POS, height=1, width = 10, bg="black", foreground="white")
    GST.place(x=605, y=305)
    GT = Label(POS, height=1, width = 10, bg="black", foreground="white")
    GT.place(x=605, y=330)

    POS.mainloop()

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    currentDT = datetime.datetime.now()
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    with open('/home/pi/Documents/Log Files/temp.txt', 'a')as f:
        f.write(currentDT.strftime("%H:%M:%S") + "|1|" + str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]) + "\n")
    

