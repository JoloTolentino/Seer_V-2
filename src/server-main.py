import os
import sys

# from matplotlib.pyplot import draw

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'modules'))
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'config','Communication','python','server'))


from DepthEstimator import DepthEstimator
from Detector import Detector 
# from OrientationEstimator imp

import cv2 




test = Detector(0)
cam = cv2.VideoCapture(0)

while True: 
    _,frame = cam.read()
    test.Detect(frame,draw=True)
    test.Find(frame,"umbrella")

    cv2.imshow("YOLO",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

