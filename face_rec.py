print("Kindly wait till the Camera Open!!! This May Take 2-3 Minutes Based On Processor")
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
def Face_reg_prg():
    train=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    video_capture = cv2.VideoCapture(0)# To Capture The Video From camera
     #To Train The Program    
    reshi_pic = face_recognition.load_image_file("D:\Vision Of Us\known_faces\Reshi.jpg")
    reshi_encoding = face_recognition.face_encodings(reshi_pic)[0]

    gay_pic = face_recognition.load_image_file("D:\Vision Of Us\known_faces\Gayathri.jpeg")
    gay_encoding = face_recognition.face_encodings(gay_pic)[0]

    merin_pic = face_recognition.load_image_file("D:\Vision Of Us\known_faces\Merinkanth.jpeg")
    merin_encoding = face_recognition.face_encodings(merin_pic)[0]

    yogi_pic = face_recognition.load_image_file("D:\Vision Of Us\known_faces\yogi.jpg")
    yogi_encoding = face_recognition.face_encodings(yogi_pic)[0]
    
    known_face_encoding = [ reshi_encoding,gay_encoding ,merin_encoding,yogi_encoding]
    known_face_name = ["Reshi","Gayathri","Merinkanth","Yogeshwari"]

    student = known_face_name.copy()

    face_locations=[]
    face_encoding = []
    face_name =[]

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    f=open("Attendance.csv","a+",newline='')
    lnwriter= csv.writer(f)
    while True:
        id,frame = video_capture.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=train.detectMultiScale(gray)
        for x,y,w,h in faces:
            #roi_gray = gray[y:y + h, x:x + w]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            
        small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rgb_small_frame = small_frame[:,:,::-1]
        if True:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encoding = face_recognition.face_encodings(rgb_small_frame,face_locations)
            face_name = []
            for face_encoding in face_encoding:
                matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
                name=""
                face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
                
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_face_name[best_match_index]
                else:
                    name="U"
                face_name.append(name)
                if name in known_face_name:
                    if name in student:
                        student.remove(name)
                        print(name+"  Present")
                        now1 = datetime.now()
                        current_time = now1.strftime("%H-%M-%S")
                        lnwriter.writerow([name,current_date,current_time])
                else:
                        print("Unknown")
                
            cv2.imshow("attendence system",frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
    for i in student:
        print(i,"Absent")
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()
    
    f1=open("Attendance.csv","r")
    for i in f1:
        txt=open("D:\Vision Of Us\_store\_file.txt","a+")
        txt.write(i)
    print("Sucess")
Face_reg_prg()
