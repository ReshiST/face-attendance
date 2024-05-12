print("Kindly wait till the Camera Open!!! ")
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
def Face_reg_prg():
    train=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    video_capture = cv2.VideoCapture(0)# To Capture The Video From camera
    
    face_locations=[]
    face_encoding = []
    face_name =[]
    recognizer = cv2.face.LBPHFaceRecognizer_create();
    recognizer.read('D:\Vision Of Us\Trainer.yml');
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    f=open("Attendance.csv","a+",newline='')
    lnwriter= csv.writer(f)
    while True:
        id,frame = video_capture.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=train.detectMultiScale(gray)
        for x,y,w,h in faces:
            roi_gray = gray[y:y + h, x:x + w]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            id, conf = recognizer.predict(roi_gray)
        
            if (conf < 50):
                if (id == 1):
                    id = 'Reshi'
                    print(id+" Present")
                elif (id==2):
                    id="Appa"
                    print(id+" Present")
            else:
                id = 'Unknown, can not recognize'
                flag = flag + 1
                break
            cv2.imshow("attendence system",frame)
            if cv2.waitKey(1) & 0xFF == ord('r'):
                    break
            
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()
    
    f1=open("Attendance.csv","r")
    for i in f1:
        txt=open("D:\Vision Of Us\_store\_file.txt","a+")
        txt.write(i)
    print("Sucess")
Face_reg_prg()
