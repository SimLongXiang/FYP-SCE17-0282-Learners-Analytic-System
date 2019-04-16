#! /usr/bin/env python

# --------------------------------------------------------------------------------------------- #
# ------------------- GUI INTERFACE FOR RASPBERRY PI : CONNECTION MANAGER ----------------------- #
# --------------------------------------------------------------------------------------------- #

# author       : Sim Long Siang
# started      : 29.12.2017
# last updated : 


"""
  --- Description ---
  
    -> Creates a GUI interface for CONNECTION MANAGER
        1. Show connected RPIs
        2. Open log files by each connection
        3. Show errors made by RPIs
        4. Plot analysis graphs
  
"""
import datetime
import tkinter as Tk
import sys, os, subprocess, traceback
from socket import *
from time import sleep
from tkinter import font
from threading import Thread


# Defining server address and port
host = '192.168.1.18'  
port = 16000 #Use port > 1024, below it all are reserved
  
class RPiSenseHat(Tk.Frame):
    
    def __init__(self, master):
        Tk.Frame.__init__(self, master)
        self.master = master

        # Setting colors for Sense Hat : RGB LEDs Matrix
        # [R, G, B, R+G, G+B, R+B, R+G+B] : Basic Colors 
        self.dark = (0, 0, 0)
        self.r = (255, 0, 0)
        self.g = (0, 255, 0)
        self.b = (0, 0, 255)
        self.rg = (255, 255, 0)
        self.gb = (0, 255, 255)
        self.rb = (255, 0, 255)
        self.rgb = (255, 255, 255)
        self.color = (0, 0, 0)

        self.currentDT = datetime.datetime.now()
        self.startGUI()
        t = Thread(target=self.Conn_init).start()

    def Analysis(self):
        os.system('sudo python3 /home/pi/Documents/Analysis.py')
            
    def startGUI(self):

        # Settings
        helv14 = font.Font(family='Helvetica', size=14, weight='bold')
        helv10 = font.Font(family='Helvetica', size=10, weight='bold')
        self.master.title("RPi Connection Manager")
        self.master.geometry("500x440")
        
        # Text : For displaying of connection outputs
        Tk.Label(text="Connected Raspberry Pi", font=helv14).pack(anchor="w", padx = 50, pady=(5,0))
        self.ConnFR = Tk.Frame()
        self.ConnOutput = Tk.Text(self.ConnFR, height=11, width=37, bg="black", foreground= "white",)
        self.ConnSB = Tk.Scrollbar(self.ConnFR, command="self.ConnOutput.yview")
        self.ConnOutput.config(yscrollcommand="self.ConnSB.set")

        self.ConnFR.pack(anchor="w", padx = 20)
        self.ConnSB.pack(side="right", fill="y")
        self.ConnOutput.pack(side="right")

        # Button : Different Function
        self.button1 = Tk.Button(bg = 'white', text="Open Log Files", height = 2, width = 15, command = lambda: subprocess.Popen(['xdg-open', '/home/pi/Documents/Log Files']), font=helv10)
        self.button1.place(x=330, y =40)
        self.button2 = Tk.Button(bg = 'white', text="Analysis", height = 2, width = 15,font=helv10, command = lambda: self.Analysis() )
        self.button2.place(x=330, y =90)
        self.button3 = Tk.Button(bg = 'white', text="Exit", height = 2, width = 15, command = lambda: os._exit(0), font=helv10)
        self.button3.place(x=330, y =140)

        # Checkboxes : for checking connection
        self.checkbox = []
        self.CK1 = Tk.Frame(height=4, width=37)
        self.CK1.pack(anchor="w", padx = 10)
        self.Check1 = Tk.Checkbutton(self.CK1, text = "RPI1", state="disabled", disabledforeground="black")
        self.Check1.pack(side = "left",padx = 3)
        self.checkbox.append(self.Check1)
        self.Check2 = Tk.Checkbutton(self.CK1, text = "RPI2", state="disabled", disabledforeground="black")
        self.Check2.pack(side = "left",padx = 3)
        self.checkbox.append(self.Check2)
        self.Check3 = Tk.Checkbutton(self.CK1, text = "RPI3", state="disabled", disabledforeground="black")
        self.Check3.pack(side = "left",padx = 3)
        self.checkbox.append(self.Check3)
        self.Check4 = Tk.Checkbutton(self.CK1, text = "RPI4", state="disabled", disabledforeground="black")
        self.Check4.pack(side = "left",padx = 3)
        self.checkbox.append(self.Check4)
        self.Check5 = Tk.Checkbutton(self.CK1, text = "RPI5", state="disabled", disabledforeground="black")
        self.Check5.pack(side = "left",padx = 3)
        self.checkbox.append(self.Check5)

        self.CK2 = Tk.Frame(height=4, width=37)
        self.CK2.pack(anchor="w", padx = 10)
        self.Check6 = Tk.Checkbutton(self.CK2, text = "RPI6", state="disabled", disabledforeground="black")
        self.Check6.pack(side = "left",padx = 3)
        self.checkbox.append(self.Check6)
        self.Check7 = Tk.Checkbutton(self.CK2, text = "RPI7", state="disabled", disabledforeground="black")
        self.Check7.pack(side = "left",padx = 3)
        self.checkbox.append(self.Check7)
        self.Check8 = Tk.Checkbutton(self.CK2, text = "RPI8", state="disabled", disabledforeground="black")
        self.Check8.pack(side = "left",padx = 3)
        self.checkbox.append(self.Check8)
        self.Check9 = Tk.Checkbutton(self.CK2, text = "RPI9", state="disabled", disabledforeground="black")
        self.Check9.pack(side = "left",padx = 3)
        self.checkbox.append(self.Check9)
        self.Check10 = Tk.Checkbutton(self.CK2, text = "RPI10", state="disabled", disabledforeground="black")
        self.Check10.pack(side = "left",padx = 3)
        self.checkbox.append(self.Check10)
        
        # Text : For displaying of error outputs
        Tk.Label(text="Error Output", font=helv14).pack()
        self.ErrorFR = Tk.Frame()
        self.ErrorOutput = Tk.Text(self.ErrorFR, height=11, width=70, bg="black", foreground= "white",)
        self.ErrorSB = Tk.Scrollbar(self.ErrorFR, command="self.ErrorOutput.yview")
        self.ErrorOutput.config(yscrollcommand="self.ErrorSB.set")

        self.ErrorSB.pack(side="right", fill="y")
        self.ErrorOutput.pack(anchor="w")
        self.ErrorFR.pack(anchor="w", padx = 20)
        
       

    def Conn_init(self) :
        self.ConnOutput.insert("end", "Initialising")
        number = 3
        while number != 0:
            self.ConnOutput.insert("end", ".")
            sleep(1)
            number -= 1
        self.ConnOutput.insert("end", "Done.")
        sock = socket() #Creating socket object
        sock.bind((host, port)) #Binding socket to a address.
        sock.listen(5) #Listening at the address
        self.ConnOutput.insert("end", "\nWaiting for Client...\n")

        while True:
            conn, addr = sock.accept() #Accepting incoming connections
            
            num = conn.recv(1024).decode()
            self.checkbox[int(num)-1].toggle()
            self.ConnOutput.insert("insert", "-- RPI" + str(num) + " Connected.\n")
            self.ConnOutput.insert("insert", str(addr) + "\n")
            self.ConnOutput.see("insert")
            Thread(target=self.clientthread, args=(conn, int(num),)).start()
            
    def clientthread(self, conn, client):
    #infinite loop so that function do not terminate and thread do not end.
     while True:
         try:
             conn.send(bytes('Hi', 'utf-8')) #send to check connection
             data = conn.recv(1024).decode() #Receiving from client
             if data != "" :
                 filepath = '/home/pi/Documents/Log Files/RPI' + str(client) + '.txt'
                 print(filepath)
                 with open(filepath, 'a') as wl:
                     wl.write(self.currentDT.strftime("%H:%M:%S")+ "|" + str(client) + "|" + data + "\n")
                 self.ErrorOutput.insert("insert", "RPI" + str(client) + " - " + str(data) + "\n")
                 self.ErrorOutput.see("insert")
         except Exception as e:
                print (e)
                self.ConnOutput.insert("insert", "XX RPI" + str(client) + " Disconnected.\n")
                self.ConnOutput.see("insert")
                self.checkbox[int(client)-1].toggle()
                conn.close()
                break
           
         
if __name__ == "__main__":
    
    root = Tk.Tk()
    app = RPiSenseHat(root) 
    root.mainloop()


# -------------------------------------------- end - of - file ----------------------------------------------------- #
