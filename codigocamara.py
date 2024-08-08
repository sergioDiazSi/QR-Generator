import cv2
import numpy as np 

video_url = 'http://192.168.1.25:8080/video'
capture = cv2.VideoCapture(video_url)

if not capture.isOpened():
    raise IOError("La camara no se puede abrir")

while(capture.isOpened()):
    ret, frame = capture.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    if(cv2.waitKey(1) == ord ('s')):
        break
    qrDetector = cv2.QRCodeDetector()
    data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)
    if len(data) > 0:
        print(f'Dato: {data}')
        cv2.imshow('webCam', rectifiedImage)
    else:
        cv2.imshow('webCam', frame)
capture.release()
cv2.destroyAllWindows
