import numpy as np
import cv2

#this is the cascade we just made. Call what you want
cascade = cv2.CascadeClassifier('./cascade-fosforo-60-93-19-stage.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # add this
    # image, reject levels level weights.
    fosforo = cascade.detectMultiScale(gray, 1.2, 3)
    
    # add this
    for (x,y,w,h) in fosforo:
        font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(img,'Fosforo',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
        cv2.putText(img,'Fosforo',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()