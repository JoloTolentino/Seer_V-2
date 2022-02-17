import socket
import cv2
import numpy as np 
import socket 
import struct


class Client: 
    
    MAX_DGRAM = 2**16
    def __init__(self,socket,port = 5000,address = "192.168.0.3"): #IP
        self.Socket = socket
        self.Port = port 
        self.Addr = address 
      
    def frame_buffer(self):
        while True:
            data,addr = self.Socket.recvfrom(self.MAX_DGRAM)
            if struct.unpack("B", data[0:1])[0]==1:
                print("Transmission Terminated")
                break
            


##TEST


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',12345))
test = Client(sock)
dat = b''
test.frame_buffer()

while True:
    seg, addr = sock.recvfrom(2**16)
    if struct.unpack("B", seg[0:1])[0] > 1:
        dat += seg[1:]
    else:
        dat += seg[1:]
        img = cv2.imdecode(np.fromstring(dat, dtype=np.uint8), 1)
        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        dat = b''
cv2.destroyAllWindows()
sock.close()
