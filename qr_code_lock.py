import RPi.GPIO as GPIO
import time
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import multiprocessing  

# opencv setup
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)

def unlock(seconds):
    #GPIO setup
    pin = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #unlock 
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(seconds)
    #lock
    GPIO.output(pin, GPIO.LOW)    
    GPIO.cleanup()

def read_qr( barcode):
    data = barcode.data.decode('utf-8')
    print(data)  
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
    pts2 = barcode.rect
    cv2.putText(frame, data, (pts2[0], pts2[1]), font, 0.9, (255, 0, 255), 2)
    #return data == 'scanned qr'
    
while True:
    success, frame = cap.read()
    
    for barcode in decode(frame):

        pool = multiprocessing.Pool()
        result_read = pool.map(read_qr, [barcode])           
        # return data == 'scanned qr' -> unlock
        result_lock = pool.map(unlock,[3])
        
        
    cv2.imshow('QR_SCAN', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break




