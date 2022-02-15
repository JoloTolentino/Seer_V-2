import cv2



cam = cv2.VideoCapture("http://192.168.0.101:4747/video")

while True:
    _,frame = cam.read()
    cv2.imshow("feed",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
