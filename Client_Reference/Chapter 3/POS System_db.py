import sys, traceback
from tkinter import *
import time
import mysql.connector
    
try:
    POS = Tk()
    st=StringVar()
    gst=StringVar()
    gt=StringVar()
    food = []
    cost = []
    subtotal = 0
    GST = 0
    grandtotal = 0
    

    def pricing(price):
        global subtotal
        global grandtotal
        subtotal = subtotal + float(price)
        GST = round(0.07 * subtotal, 2)
        grandtotal = round(subtotal + GST, 2)
        st.set(subtotal)
        gst.set(GST)
        gt.set(grandtotal)
    
    def orderlist(item, price):
        global food, cost
        ShowOrder.insert(INSERT, item + "\n")
        ShowPrice.insert(INSERT, price + "\n")
        food.append(item)
        cost.append(price)
        pricing(price)

    def clearlist():
        global subtotal, grandtotal, food ,cost
        
        ShowOrder.delete(1.0, END)
        ShowPrice.delete(1.0, END)
        food.clear()
        cost.clear()
        st.set("")
        gst.set("")
        gt.set("")
        subtotal = 0
        grandtotal = 0

    def submit():
        global time, food, cost
        messagebox.showinfo("Receipt", "Final Receipt\n\n" + ShowOrder.get(1.0, END) + "Grand Total : S$" + str(grandtotal))
        time = time.strftime('%Y-%m-%d %H:%M:%S')
        
        connection = mysql.connector.connect( host='localhost', user='root', db='Orders')
        cursor = connection.cursor()

        print(food, cost)
        for x in range(0,len(food)):

            ### INSERT DATABASE VALUES CODE BELOW ###
            cursor.execute("INSERT INTO UserOrder (hhmmss,item, price) VALUES (%s, %s, %s)", (time, food[x], cost[x]))
            connection.commit()
            
        connection.close()
        clearlist()

    def log():
    
        top = Toplevel()
        top.title("History of Orders")
        top.geometry("470x300+20+20")

        Label(top, text="History of Orders", font=("Helvetica", 18)).grid(column=2,row=0,padx=50)
        HisOrder = Text(top, height=16, width = 52, foreground="black")
        HisOrder.grid(column=2,row=2,padx=50)
        connection = mysql.connector.connect( host='localhost', user='root', db='Orders')
        cursor = connection.cursor()

        ### INSERT INSTRUCTION TO QUERY DATABASE CODE BELOW ###
        cursor.execute("SELECT * FROM UserOrder WHERE price > 10 ORDER BY CONVERT(price, SIGNED INTEGER)")
        
        for (hhmmss, item, price) in cursor:

            HisOrder.insert(INSERT,str(hhmmss) + "  " + item + "\n")
            HisOrder.tag_add("last", HisOrder.index("end"))
            HisOrder.tag_config("last", justify="right")
            HisOrder.insert(INSERT,price + "\n", "last")
            
        connection.close()
        
    POS.title("Nexus Cafe POS system")
    POS.geometry("700x380+50+50")

    Label(POS, text="Cafe Menu", font=("Helvetica", 18)).place(x=120, y=1)
    Label(POS, text="Food Order", font=("Helvetica", 18)).place(x=480, y=1)

    SB = LabelFrame(POS, text="Small Bites", height=100, width=300, bg="yellow")
    SB.place(x=15, y=30)
    TF = Button(SB, text="Truffles Fries\nS$5", height=3, width=12, command=lambda: orderlist("Truffles Fries", "5"))
    TF.grid(padx=5, pady=5)
    CW = Button(SB, text="Chicken Wings\nS$7", height=3, width=12, command=lambda: orderlist("Chicken Wings", "7"))
    CW.grid(column=1,row=0, padx=5, pady=5)
    CL = Button(SB, text="Calamari\nS$5", height=3, width=12, command=lambda: orderlist("Calamari", "5"))
    CL.grid(column=2,row=0, padx=5, pady=5)

    SB = LabelFrame(POS, text="Mains", height=100, width=300, bg="blue")
    SB.place(x=15, y=120)
    TF = Button(SB, text="Salted Egg Prawn Pasta\nS$13", height=3, width=12, wraplength=80, command=lambda: orderlist("Salted Egg Prawn Pasta", "13"))
    TF.grid(padx=5, pady=5)
    CW = Button(SB, text="Aglio Olio\nS$6.50", height=3, width=12, command=lambda: orderlist("Aglio Olio", "6.50"))
    CW.grid(column=1,row=0, padx=5, pady=5)
    CL = Button(SB, text="Carbonara\nS$8", height=3, width=12, wraplength=80, command=lambda: orderlist("Carbonara", "8"))
    CL.grid(column=2,row=0, padx=5, pady=5)
    P = Button(SB, text="Sirloin Steak\nS$17", height=3, width=12, command=lambda: orderlist("Sirloin Steak", "17"))
    P.grid(row=1, padx=5, pady=5)
    MS = Button(SB, text="Black Pepper Chicken Chop\nS$12", height=3, width=12, wraplength=100, command=lambda: orderlist("Black Pepper Chicken Chop", "12"))
    MS.grid(column=1,row=1, padx=5, pady=5)
    GB = Button(SB, text="Grilled Salmon\nS$14", height=3, width=12, command=lambda: orderlist("Grilled Salmon", "14"))
    GB.grid(column=2,row=1, padx=5, pady=5)

    SB = LabelFrame(POS, text="Drinks and Dessert", bg="green")
    SB.place(x=15, y=280)
    TF = Button(SB, text="Ice Cream Waffles\nS$7", height=3, width=12, wraplength=80, command=lambda: orderlist("Ice Cream Waffles", "7"))
    TF.grid(padx=5, pady=5)
    CW = Button(SB, text="Coke/Sprite/Root Beer Float\nS$3", height=3, width=12, wraplength=110, command=lambda: orderlist("Coke/Sprite/Root Beer Float", "3"))
    CW.grid(column=1,row=0, padx=5, pady=5)
    CL = Button(SB, text="Canned Drinks\nS$1.50", height=3, width=12, wraplength=100, command=lambda: orderlist("Canned Drinks", "1.50"))
    CL.grid(column=2,row=0, padx=5, pady=5)

    Submit = Button(POS, text="Submit", height=2, width=3, command=lambda: submit())
    Submit.place(x=425, y=270)
    Clear = Button(POS, text="Clear", height=2, width=3,command=lambda: clearlist())
    Clear.place(x=480, y=270)
    History = Button(POS, text="History", height=2, width=3,command=lambda: log())
    History.place(x=455, y=315)
    

    ShowOrder = Text(POS, height=16, width = 30, bg="black", foreground="red")
    ShowOrder.place(x=430, y=35)
    ShowPrice = Text(POS, height=16, width = 5, bg="black", foreground="red")
    ShowPrice.place(x=650, y=35)
    
    Label(POS, text="Sub-total:").place(x=540, y=280)
    Label(POS, text="GST (7%):").place(x=540, y=305)
    Label(POS, text="Grand-total:").place(x=525, y=330)
    ST = Label(POS, height=1, width = 10, bg="black", textvariable=st, foreground="white")
    ST.place(x=605, y=280)
    GST = Label(POS, height=1, width = 10, bg="black", textvariable=gst, foreground="white")
    GST.place(x=605, y=305)
    GT = Label(POS, height=1, width = 10, bg="black", textvariable=gt, foreground="white")
    GT.place(x=605, y=330)

    POS.mainloop()

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print("error in line" , exc_tb.tb_lineno ,"|", sys.exc_info()[0] , "|", sys.exc_info()[1])
    with open('/home/pi/Documents/Log Files/temp.txt', 'w')as f:
        f.write(str(exc_tb.tb_lineno) + "|" + str(sys.exc_info()[0]) + "|" + str(sys.exc_info()[1]))
    

