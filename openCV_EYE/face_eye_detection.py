import sys
import numpy as np
import cv2
import time
import csv
import logging
import datetime

all_count = 0     #Checking finding count
true_count = 0    #Checking detection count

def mylog(start_time, end_time, count):   #show real-time result
    print ('st:%s, et:%s, cnt:%s', start_time, end_time, count)

#open result CSV file
file = open('./result/res_Insert_name.csv', 'w')

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

one_m_timer_start = time.time()
while 1:
    s = time.clock()  #Start time
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    all_count = all_count + 1  #Plus finding count

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        true_count = true_count + 1
        e = time.clock()  #Finish time
        msg = str(s) + ',' + str(e) + ',' + str(e-s) + ',' + str(true_count) +'\n'
        file.write(msg)  #writing about start time, end time, spend time, face detection count

        mylog('','',msg)

    one_m_timer_end = time.time()
    if( one_m_timer_end - one_m_timer_start > 10 ):   #10seconds program run
        print one_m_timer_end - one_m_timer_start
        break

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff  #If you press "ESC" button on your keyboard program is end
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
file.close()

print "All count :" , all_count    #show all_count
print "Detection count :" , true_count    #show detection count
