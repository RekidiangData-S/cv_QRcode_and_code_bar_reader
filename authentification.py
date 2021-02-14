import cv2
import numpy as np
from pyzbar.pyzbar import decode
import sqlite3

# open database #########################
conn = sqlite3.connect('agent.db')
#create cursor
c = conn.cursor() #create a cursor
b= conn.cursor()
# Qeury the database
c.execute("SELECT ID FROM  people")
b.execute("SELECT * FROM  people")
print(b.fetchall())
print(c.fetchall()[0])
db = c.fetchall()

##########################################
#img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()
while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        myData = int(myData)
        #print(myData)
        if myData in db[0]:
            myOutput = 'Authorized'
            myColor = (0,255,0)
            print('Authorized')
        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)
            print('Un-Authorized')
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,myColor,2)
    cv2.imshow('Result',img)
    cv2.waitKey(1)