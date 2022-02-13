## Author          : Jolo Tolentino
## Project Name    : SEER-V2
## Project Started : January 25,2022



### DepthEstimator.py uses the MiDas Depth prediction Model (model-f6b98070.onnx) 

from git import Blob
import numpy as np
import OrientationEstimator 
import Detector
import os 
import cv2 
import yaml 



class DepthEstimator:
    def __init__(self):
        print("Seer - Server Initializing .....")
        CFG_File = open(str(os.path.dirname(os.getcwd())+'\config\config.yaml'))
        Parsed_CFG = yaml.load(CFG_File,Loader=yaml.FullLoader)[0]
        
        # print(Parsed_CFG)
        #Loading Height Approximates
        Estimated_Heights_File =  open(str(os.path.dirname(os.getcwd())+'\data\YAML\heights.yaml'))
        self.Estimated_Heights_Data = yaml.load(Estimated_Heights_File,Loader=yaml.FullLoader)[0]

        #Camera Settings
        self.camera_settings = Parsed_CFG["Camera Config"]
        self.camera_name = self.camera_settings["Camera Name"]
        self.field_of_view = self.camera_settings["Field of View"]
        self.focal_length = self.camera_settings["Focal Length"]
        
        print("Running Configuration Settings for : "+ self.camera_name )
        
        self.LoadModel(Parsed_CFG["model"])
        self.Detector = Detector()


        ## Open Camera
       

    def LoadModel(self,model_name):
        print("Loading Depth Model...")

        self.model = cv2.dnn.readNet(model_name)
        self.model.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.model.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        if self.model:
            print("Model Loaded.")
        else:
            print("Model Not Found. Program is Now Exiting....")
            return 0 
  
    def Comparative_Analysis(self,Known,Known_h, target):
        #Based on Estimated Heights we estimate the distance of the target object 
        if Known in self.Estimated_Heights_Data:   
            self.KnownDistance = (self.Estimated_Heights_Data[Known]*self.focal_length)/ (Known_h*10)
            TargetCoords = Detector.find(target)
            RefCoords = Detector.find(Known) 
        else:
            print("No Refference Object.")
        
        # We then take in Coordinates of the target
        
        # Place target Data
        self.targetDistance = (self.KnownDistance* self.DepthMap[TargetCoords[0],TargetCoords[1]])/self.DepthMap[RefCoords[0],RefCoords[1]]





    def DepthMap(self, stream, Display = False): 
        
        Height,Width = stream.shape[0],stream.shape[1]
        RGB_Stream = stream[:,:,::-1] #Takes in OPENCV BGR input
        Binary_Large_Object= cv2.dnn.blobFromImage(RGB_Stream,1/255.,(384,384),(123.675, 116.28, 103.53), True, False)
        self.model.setInput(Binary_Large_Object)
        self.output = self.model.forward()

        self.output = self.output[0,:,:]
        self.output = cv2.resize(self.output, (Width, Height))
        self.output = cv2.normalize(self.output, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)


        


      



    