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

    
    def Median_Filter(self):
        pass
    
    
    def Find_2D_Height(self,stream):

        with self.objectron.Objectron(static_image_mode =False,
                                    max_num_objects = 1,
                                    min_detection_confidence = 0.5,
                                    min_tracking_confidence = 0.99,
                                    model_name = self.Target_Object) as objctron:
            stream.flags.writeable = False
            stream = cv2.cvtColor(stream,cv2.COLOR_BGR2RGB)
            results = objctron.process(stream)

            self.Rotation_Matrix = results.detected_objects.rotation
            self.Object_Landmarks = results.detected.landmarks_2D
            self.ThreeD_Bounding_Box = self.objectron.BOX_CONNECTIONS

            self.Euler_Angles()







    def Euler_Angles(self):
        self.Pitch()
        self.Roll()



    def Pitch(self): #rotation about the y axis
        self.Yaw()
        self.pitch = math.atan2(-1*self.Rotation_Matrix[2][0],self.Rotation_Matrix[0][0]) if self.yaw!=0 else  math.atan2(-1*self.Rotation_Matrix[2][0],self.Rotation_Matrix[1][0])
        print(self.pitch)
    def Yaw(self): #rotation about the z axis
        self.yaw  = math.atan2(self.Rotation_Matrix[1][0],self.Rotation_Matrix[0][0]) 
        print(self.yaw)
    def Roll(self): # rotation about the x axis
        self.roll = math.atan2(self.Rotation_Matrix[2][1],self.Rotation_Matrix[2][2]) 
        print(self.roll)


    


