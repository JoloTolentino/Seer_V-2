## Author          : Jolo Tolentino
## Project Name    : SEER-V2
## Project Started : January 25,2022



### Detecor.py uses the YOLO object detection model by default but can be changed

import numpy as np 
import os 
import cv2 
import yaml 



class Detector:
    def __init__(self):
        CFG_File = open(str(os.path.dirname(os.getcwd()+'\config\config.yaml')))
        Parsed_CFG = yaml.load(CFG_File,Loader=yaml.FullLoader)

        #Load Yolo Model
        Yolo_Model_CFG = Parsed_CFG['Yolo CFG']
        Yolo_Model_Weights = Parsed_CFG['Yolo Weights']
        Yolo_Model_Names = Parsed_CFG['Yolo Names']

        #Scaling 
        self.Image_Scale = Parsed_CFG["Image Scale"]


        self.Yolo_Model = cv2.dnn.readNetFromDarknet(Yolo_Model_CFG,Yolo_Model_Weights)

        if self.Yolo_Model:
            print("Object Detection Model Loaded")
        else: 
            print("Object Detection Model Not Found...")




    def Detect(self,data):
        self.BLOB = cv2.dnn.blobFromImage(data,)



    def Find(self):
        pass


        