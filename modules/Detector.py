## Author          : Jolo Tolentino
## Project Name    : SEER-V2
## Project Started : January 25,2022



### Detecor.py uses the YOLO object detection model by default but can be changed


import numpy as np 
import os 
import cv2 
import yaml 
import configparser as cfg


class Detector:
    def __init__(self,threshold):
        CFG_File = open(str(os.path.dirname(os.getcwd())+'\config\config.yaml'))
        Parsed_CFG = yaml.load(CFG_File,Loader=yaml.FullLoader)[0]

        #Load Yolo Model Configurations from CFG file
        Yolo_Model_CFG = Parsed_CFG['Yolo CFG']
        Yolo_Model_Weights = Parsed_CFG['Yolo Weights']
        Yolo_Names_Directory= Parsed_CFG['Yolo Labels']
                

        with open(Yolo_Names_Directory) as names:
            self.Yolo_Labels = [name.rstrip() for name in names]

      
        self.Yolo_Labels_Indexing = {label:index for index,label in enumerate(self.Yolo_Labels)} #Reverse Dict
        ##
        self.Thresh = threshold

        #Load Model onto memory using OpenCV
        self.Yolo_Model = cv2.dnn.readNetFromDarknet(Yolo_Model_CFG,Yolo_Model_Weights)


        if self.Yolo_Model:
            print("Object Detection Model Loaded")
            Layer_Names = self.Yolo_Model.getLayerNames()
            self.Necessary_Layers = [Layer_Names[layers-1] for layers in self.Yolo_Model.getUnconnectedOutLayers()] 
        else: 
            print("Object Detection Model Not Found...")



    def Detect(self,data, draw = False):
        
        # STORAGE VARIABLES Initialize every Use when detecting
        self.Boxes, self.Confidences, self.Classification_ID = [],[],[]
        self.Height,self.Width = data.shape[0],data.shape[1]
        #Blob from Image preprocesses input data (mean subtraction, normalizing(Image Scale Factor), OPTIONAL (Channel Swapping))
        self.BLOB = cv2.dnn.blobFromImage(data,1/255,(416,416),swapRB = True)
        self.Yolo_Model.setInput(self.BLOB)
        self.Predictions = self.Yolo_Model.forward(self.Necessary_Layers)

        for predictions in self.Predictions:
            for objects in predictions: 

                Scores = objects[5:]
                Classification = np.argmax(Scores)
                Confidence  = Scores[Classification]

                if Confidence>self.Thresh:
                    Box = objects[:4]*np.array([self.Width,self.Height,self.Width,self.Height])
                    (CenterX,CenterY,Width,Height) = Box.astype('int')
                    XMin, YMin = CenterX-Width//2 , CenterY-Height//2
                    

                    self.Boxes.append([XMin,YMin,Width,Height])
                    self.Confidences.append(float(Confidence))
                    self.Classification_ID.append(Classification)
                    print(self.Yolo_Labels[Classification])


        self.Indexes=cv2.dnn.NMSBoxes(self.Boxes,self.Confidences,self.Thresh,self.Thresh)

        if draw: 
            self.OverLay(data)
            

    def OverLay(self,CameraFeed):
        VideoFeed = CameraFeed.copy()
        try:
            for i in self.Indexes.flatten():
                (x, y) = (self.Boxes[i][0],self.Boxes[i][1])
                (w, h) = (self.Boxes[i][2], self.Boxes[i][3])          
                cv2.rectangle(VideoFeed, (x, y), (x + w, y + h), (255,255,0), 2)
                text = "{}: {:.2f}".format(self.Yolo_Labels[self.Classification_ID[i]], self.Confidences[i])
                cv2.putText(CameraFeed, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0) , 2)  
                cv2.imshow("Height Display",VideoFeed)

        except: 
            text = "Model has low confidence in the Environment...."
            cv2.putText(VideoFeed, text, (0, 10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0) , 2)  
            cv2.imshow("Height Display",VideoFeed)
       

    def Find(self,target,draw = False):
        Target_Index = self.Yolo_Labels_Indexing[target] 
        if Target_Index in self.Classification_ID:
            Indexes = np.where(np.array(self.Classification_ID) == Target_Index)[0] ##an array of indexes
            
            









            


            

