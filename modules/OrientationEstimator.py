## Author          : Jolo Tolentino
## Project Name    : SEER-V2
## Project Started : January 25,2022



### We use Pose Estimation to understand angle orientation of Objects, with Google's Objectron dataset 
### We recognize angle orientation of desired Target Objects


import yaml
import mediapipe as mp 
import math 
import cv2 
import os 


class AngleRotation:
    def __init__(self,ObjectRefference):
        CFG_File = open(str(os.path.dirname(os.getcwd())+'\config\config.yaml'))
        Parsed_CFG = yaml.load(CFG_File,Loader=yaml.FullLoader)[0]

        #Loads Known Objects
        self.Known_Objects= ["Cup","Shoe"]
        self.Target_Object = ObjectRefference

        if self.Target_Object not in self.Known_Objects:
            return print('Pls, use a different object')

        print('Estimating Angle....')

        self.drawing = mp.solutions.drawing_utils
        self.objectron = mp.solutions.objectron

    def Find(self):
         


    def Pitch(self): #rotation about the y axis
        self.Yaw()
        self.pitch = math.atan2(-1*self.Rotation_Matrix[2][0],self.Rotation_Matrix[0][0]) if self.yaw!=0 else  math.atan2(-1*self.Rotation_Matrix[2][0],self.Rotation_Matrix[1][0])

    def Yaw(self): #rotation about the z axis
        self.yaw  = math.atan2(self.Rotation_Matrix[1][0],self.Rotation_Matrix[0][0]) 

    def Roll(self): # rotation about the x axis
        self.roll = math.atan2(self.Rotation_Matrix[2][1],self.Rotation_Matrix[2][2]) 



    


