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
        self.KnownObjects= Parsed_CFG['6D Objects']
        self.TargetObect = ObjectRefference

        if self.TargetObect not in self.KnownObjects:
            return print('Pls, use a different object')
             

    # def Orientation(self,Rotation_Matrix,feed):
    #     ###Center Coordinates
        
    def Pitch(self):
        
        self.pitch = math.atan2(self.) 
        
        pass

    def Yaw(self):
        pass

    def Roll(self):
        pass



    


