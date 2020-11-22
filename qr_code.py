import cv2
import numpy as np
from pyzbar.pyzbar import decode

#frame = cv2.imread('qr.png')
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:

    success, frame = cap.read()
    for barcode in decode(frame):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(frame, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)

    cv2.imshow('Result', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
