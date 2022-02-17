## Author          : Jolo Tolentino
## Project Name    : SEER-V2
## Project Started : January 25,2022



### UDP_Server.py (Video Source ex. Jetson Xavier, raspberry pi and etc...) was created to transmit data for remote computation()



import socket
import cv2
import numpy as np 
import math
import struct


class Server:
    
    MAX = 2**16
    MAX_ERROR = MAX-64

    def __init__ (self, Socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM), Port=5000, Address = "192.168.0.3"):
        self.socket = Socket ## socket connection 
        self.port = Port
        self.addr = Address

    def UDP_Data_STREAM(self,frame):


        ## convert to smallest file type which is jpg
        stream = cv2.imencode('.jpg',frame)[1]
        ## convert jpg image array to string 
        String_Stream  = stream.tostring() 
        Size = len(String_Stream)
        Datagram_Count = Size//self.MAX_ERROR
        index = 0
        while Datagram_Count:

            last_index = min(Size,index + self.MAX_ERROR)

            self.socket.sendto(struct.pack("B",Datagram_Count)+ # converts data to bytes 
                               String_Stream[index:last_index],
                               (self.addr,self.port))

            index = last_index
            Datagram_Count-=1

    
##test

test = Server() 
cam = cv2.VideoCapture(1)

while cam.isOpened():
    _frame = cam.read() 
    test.UDP_Data_STREAM(cam)
cam.release()
cv2.destroyAllWindows()








