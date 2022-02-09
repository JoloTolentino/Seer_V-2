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

    def __init__ (self, Socket, Port, Address = "127.0.0.1"):
        self.socket = Socket ## socket connection 
        self.port = Port
        self.addr = Address

    def UDP_STREAM(self,frame):


        ## convert to smallest file type which is jpg
        stream = cv2.imencode('.jpg',frame)[1]
        ## convert jpg image array to string 
        String_Stream  = stream.tostring() 
        Size = len(String_Stream)
        Datagram_Count = Size//self.MAX_ERROR
        index = 0
        while Datagram_Count:

            last_Index = min(Size,index + self.MAX_ERROR)

            self.socket.sendto(struct.pack("B",Datagram_Count)+ # converts data to bytes 
                               String_Stream[]) 





