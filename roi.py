import numpy as np
import cv2

from matplotlib import pyplot as plt
def sketch_transform(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale

cap = cv2.VideoCapture(0)

#Get dimensions
ret, frame = cap.read()
width, height, channel = frame.shape
upper_left = (0, 0)
bottom_right = (240, 320)
print({height} , {width})
cv2.destroyAllWindows()

while True:
    ret, frame = cap.read()
    print(frame.shape)
    
    #Rectangle marker
    r = cv2.rectangle(frame, upper_left, bottom_right, color=(255,0,0))
    rect_img = frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
    
    sketcher_rect = rect_img
    sketcher_rect = sketch_transform(sketcher_rect)
    
    #Conversion for 3 channels to put back on original image (streaming)
    sketcher_rect_rgb = cv2.cvtColor(sketcher_rect, cv2.COLOR_GRAY2RGB)
    
    #Replacing the sketched image on Region of Interest
    frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = sketcher_rect_rgb
    cv2.imshow("Sketcher ROI", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 