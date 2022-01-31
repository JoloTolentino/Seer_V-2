import numpy as np 
import cv2 
import tkinter 
import math 


# KnownHeight = 138.5
# KnownWidth = 136.7
# KnownPixelHeight = 226
# KnownHeight = 111.500

# KnownHeight = 111.500
# KnownPixelHeight = 297


KnownHeight = 98.0
# KnownPixelHeight = 195
# # KnownDistance = 500
# KnownDistance = 400


# FocalLength = 812
# FocalLength = 802 #red cup 300
#852

cam = cv2.VideoCapture(1)


def FocalLength(Distance,RealHeight,PixelHeight):
    return  round((PixelHeight*Distance)/RealHeight)

def ComputedDistance(RealHeight,FocalLength,PixelHeight):
    
    return  (RealHeight*FocalLength)/(PixelHeight*10)


#Lower
def HonChange(val):
    cyanLower[0] = val 
def SonChange(val):
    cyanLower[1] = val 
def VonChange(val):
    cyanLower[2] = val 


#Upper
def UHonChange(val):
    cyanUpper[0] = val 
def USonChange(val):
    cyanUpper[1] = val 
def UVonChange(val):
    cyanUpper[2] = val 


cyanLower = np.array([0, 0,  0]).astype('uint8')
cyanUpper = np.array([255,255,255]).astype('uint8')
alpha_slider_max = 255
title_window = "TrackBar"



cv2.namedWindow(title_window)
cv2.createTrackbar("LHLim", title_window , 0, alpha_slider_max, HonChange)
cv2.createTrackbar("LSLim", title_window , 0, alpha_slider_max, SonChange)
cv2.createTrackbar("LVLim", title_window , 0, alpha_slider_max, VonChange)
cv2.createTrackbar("UHLim", title_window , 0, alpha_slider_max, UHonChange)
cv2.createTrackbar("USLim", title_window , 0, alpha_slider_max, USonChange)
cv2.createTrackbar("UVLim", title_window , 0, alpha_slider_max, UVonChange)




while True: 
    _,videoFrame = cam.read()

    rgb = cv2.cvtColor(videoFrame,cv2.COLOR_BGR2RGB)
    blurred = cv2.GaussianBlur(videoFrame,(21,21),0)
    hsv = cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    colorMask = cv2.inRange(hsv,cyanLower,cyanUpper)
    segmeneted = cv2.bitwise_and(videoFrame,videoFrame,mask=colorMask)
    

    eroded = cv2.erode(segmeneted,(13,13))
    opening = cv2.dilate(eroded,(13,13))

    openingSegmentation = cv2.cvtColor(opening,cv2.COLOR_BGR2GRAY)
    
    contours,_ = cv2.findContours(openingSegmentation,mode = cv2.RETR_TREE , method = cv2.CHAIN_APPROX_SIMPLE)
    image_copy = videoFrame.copy()
   
    try:
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        Estimated_Distance = ComputedDistance(KnownHeight,
                                             FocalLength= 812,
                                             PixelHeight = h)
        cv2.rectangle(image_copy,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.putText(image_copy,"{:.2f} mm".format(Estimated_Distance),
                org = (x-10,y-10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color = (255,255,0),
                thickness= 1)

        
        # print(Estimated_Distance)     
    except:
        pass


    cv2.imshow("blurring",blurred)
    cv2.imshow("rgb",rgb)
    cv2.imshow("originial ", videoFrame)
    cv2.imshow("segmented", opening)
    cv2.imshow("Localized", image_copy)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
