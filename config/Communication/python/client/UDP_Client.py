import socket
import numpy as np 
import socket 
import struct


class Client: 
    
    MAX_DGRAM = 2**16
    def frame_buffer(self,socket):

        while True:


