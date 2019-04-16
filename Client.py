#!usr/bin/python
from socket import *
from threading import Thread
import time


class Client(object):
        
        def __init__(self):
                self.host = '192.168.1.18' 
                self.port = 16000

                self.sock = socket() # Connecting to socket
                self.sock.connect((self.host, self.port)) 
                print("Connected !")
                self.sock.send(bytes('1' , 'utf-8'))
                time.sleep(1)
                self.ToServer()

        def ToServer(self):
                f_next_content = ""
                current  = 0
                while True:
                        #Context Manager - does clean up and closing
                        with open('RPI1.txt', 'r')as f: 
                                f_next_content = f.read().splitlines()
                                if (len(f_next_content) >  current): #Check if there is new error
                                        last_line = f_next_content[-1]
                                        if last_line != "" :
                                                self.sock.send(bytes(last_line , 'utf-8')) #Send Over to Server
                                        current += 1

if __name__ == "__main__":
        Client()
        while True:
               self.data = self.sock.recv(1024).decode() 
        self.sock.close()


