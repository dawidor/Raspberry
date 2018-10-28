import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(-1)
print cap.isOpened()
index = 1
while 1:
        ret, img = cap.read()
        print ret
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if face_cascade:
          print face_cascade
 
        roi_gray = gray       
        roi_color = gray
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            cv2.imshow("Adding faces to traning set...", img[y: y + h, x: x + w])
            filename = "data/" + str(index) + ".jpg"
            print('Write file face=', index)
            #cv2.imwrite(filename, img[y: y + h, x: x + w])
            
            cv2.imwrite(filename, img)
            index=index+1

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:            
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            #cv2.imshow('img',img)
            #cv2.imshow("Adding faces to traning set...", img[ey: ey + eh, ex: ex + ew])
        

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break


                
cap.release()
cv2.destroyAllWindows()
            

face_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_eye.xml')



