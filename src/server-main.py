import os
import sys

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'modules'))
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'config','Communication','python','server'))


from DepthEstimator import DepthEstimator
from Detector import Detector 
# from OrientationEstimator imp

import cv2 




test = Detector(0.2)
cam = cv2.VideoCapture(1)


