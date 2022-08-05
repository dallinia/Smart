from asyncio.mixins import _global_lock
import datetime
import cv2
import threading
import os
import time
from cv2 import destroyAllWindows
import keyboard
import numpy as np
from PIL import Image
import glob


path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
i = 0


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
count1 = 0
count2 = 0

k = cv2.waitKey(10) & 0xff




class showcamThread(threading.Thread): #
    def __init__(self,previewName, cam_num):
        super(showcamThread, self).__init__()
        self.previewName = previewName
        self.cam_num = cam_num
        
    def run(self): #이 함수로 캠이 켜지게 된다.
        show_cam(self.previewName, self.cam_num)
        
        
        
def show_cam(previewName, cam_num):
    global base_path
    global count1
    global id
    global k
    global count2
    


    cam = cv2.VideoCapture(cam_num)
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    video = -1 # 객체를 담을 수 있는 변수 선언(-1로 초기화한거임.)
   

    while True:
        ret, img =cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 80):
                id = id
                confidence = "  {0}%".format(round(100 - confidence))
                
                
                if (id == 1):
                    ImageOnDisplay()
                    if k == 100:#d
                        #base_path = os.path.dirname(os.path.abspath("__file__"))
                        base_path = 'image' + '/' + str(id)
                        if not os.path.exists(base_path): #이 명령어는 해당 사용자 폴더가 없을시 폴더를 자동으로 만들어 준다
                            os.makedirs(base_path)
                        write_cam_1('inside', 1)
                        print("image save")
                    
                        
                if (id == 2):
                    ImageOnDisplay()
                    if k == 100:#d
                        base_path = os.path.dirname(os.path.abspath("__file__"))
                        base_path = base_path+"\\"+'image' + '/' + str(id)
                        if not os.path.exists(base_path): #이 명령어는 해당 사용자 폴더가 없을시 폴더를 자동으로 만들어 준다
                            os.makedirs(base_path)
                        write_cam_2('inside', 1)
                        print("image save")
                    
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera' ,img) 
        cv2.imshow('camera' ,img)
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:#esc
            break
                  
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    
    
  
        
def write_cam_1(previewName, cam_num):
    global base_path
    global count1
    global id
    global count2
     

    count1 += 1
    cam = cv2.VideoCapture(1)
    video = -1 # 객체를 담을 수 있는 변수 선언(-1로 초기화한거임.)
    if cam.isOpened():
        rval, frame = cam.read()
        
    else:
        rval = False
        
    
    time.sleep(2)
    cv2.imwrite(('image' + '/' + str(id) + "/User" + '.' + str(id) + '.' + str(count1) + ".jpg"), frame)#사진이 저장되는 이름 
    
def write_cam_2(previewName, cam_num):
    global base_path
    global count1
    global id
    global count2
     

    count2 += 1
    cam = cv2.VideoCapture(1)
    video = -1 # 객체를 담을 수 있는 변수 선언(-1로 초기화한거임.)
    if cam.isOpened():
        rval, frame = cam.read()
        
    else:
        rval = False
        
    
    time.sleep(2)
    cv2.imwrite(('image' + '/' + str(id) + "/User" + '.' + str(id) + '.' + str(count2) + ".jpg"), frame)#사진이 저장되는 이름


def ImageOnDisplay():
    global id
    
    index = 0
    count11 = 0
    target_dir = "image/" + str(id) + "/"
    file_list = glob.glob(target_dir + "*.*")
    
    if (id == 1):
        for i in file_list:
            count11 += 1
            filePath = cv2.imread(file_list[index])
            filePaths = cv2.resize(filePath, (0, 0), None, .5, .5)

            cv2.imshow('image' + str(count11), filePaths)
            index += 1
            
    if (id == 2):
        for i in file_list:
            count11 += 1
            filePath = cv2.imread(file_list[index])
            filePaths = cv2.resize(filePath, (0, 0), None, .5, .5)

            cv2.imshow('image' + str(count11), filePaths)
            index += 1
            
            
    
            
           
            
    
            
            
if __name__ == "__main__":
    thread1 = showcamThread("front", 0)
    
    thread1.start()
