# coding=utf-8
import cv2
import dlib
import numpy as np
import time

detector = dlib.get_frontal_face_detector()  #使用默认的人类识别器模型
global maxnum
maxnum=0

def contrast_demo(img1, c, b):  # 亮度就是每个像素所有通道都加上b
    rows, cols, chunnel = img1.shape
    blank = np.zeros([rows, cols, chunnel], img1.dtype)  # np.zeros(img1.shape, dtype=uint8)
    dst = cv2.addWeighted(img1, c, blank, 1-c, b)
    #cv2.imshow("con_bri_demo", dst)
    return dst

def discern(img):
    global maxnum
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(gray, 1)
    
    if len(dets)> maxnum:
        maxnum=len(dets)
    if len(dets)==0:
        maxnum=0
        
    print("当前人数为{}".format(maxnum))
    for face in dets:
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        im=img[top:bottom,left:right]
        if top!=bottom and right!=left and top>0 and bottom>0 and left>0 and right>0:
            im=cv2.resize(im,(100,100),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite('/home/pi/'+str(int(round(time.time() * 1000)))+'.jpg',im)
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        imgs=cv2.resize(img,(526*2,296*2),interpolation=cv2.INTER_CUBIC)
        cv2.imshow("image", imgs)

n=0

cap = cv2.VideoCapture("/mnt/1/1.flv")
while (1):
    n=n+1
    ret, img = cap.read()
    img=contrast_demo(img,1.3,10)
    if n==150:
        
        res=cv2.resize(img,(526*8,296*8),interpolation=cv2.INTER_CUBIC)
    #print(res.shape)
    #cv2.imshow("image", res)
        discern(res)
        n=0
  #  else:
  #      cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

