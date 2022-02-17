## Author          : Jolo Tolentino
## Project Name    : SEER-V2
## Project Started : January 25,2022



### We use Pose Estimation to understand angle orientation of Objects, with Google's Objectron dataset 
### We recognize angle orientation of desired Target Objects


import yaml
import mediapipe as mp 
import cv2 



class AngleOrientation:
    def __init__(self,ObjectRefference):



        self.TargetObect = ObjectRefference

        if self.TargetObect not in self.KnownObjects:
             
        

    def Orientation(self,coordinates,BBox,feed):
        self.x,self.y,self.z = coordinates[0],coordinates[1],coordinates[2]


    def Rot_X(self) 

    


