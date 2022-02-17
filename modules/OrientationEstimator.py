## Author          : Jolo Tolentino
## Project Name    : SEER-V2
## Project Started : January 25,2022



### We use Pose Estimation to understand angle orientation of Objects, with Google's Objectron dataset 
### We recognize angle orientation of desired Target Objects


import yaml
import mediapipe as mp 
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
             

    def Orientation(self,coordinates,SixD_Bounding_Box,feed):
        ###Center Coordinates
        self.x,self.y,self.z = coordinates[0],coordinates[1],coordinates[2]
        self.Graph = SixD_Bounding_Box # takes in Graph representation where G = [V,N] where G represents a graph while V is Vertex i and its Neighbors N
        

    def Rot_X(self,yFrame,zFrame):
        pass

    def Rot_Y(self,xFrame,zFrame):
        pass

    def Rot_Z(self,xFrame,yFrame):
        pass



    


