import cv2
import numpy as np
cap=cv2.VideoCapture(-1)

while True:
    retval, img=cap.read()
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel1=np.array([[-1,0,1],
                      [-2,0,2],
                      [-1,0,1]])
    kernel2=np.array([[-1,-2,-1],
                      [0,0,0],
                      [1,2,1]])

    sharpened1=cv2.filter2D(img,-1,kernel1)
    sharpened2=cv2.filter2D(img,-1,kernel2)

    sharpened1=cv2.convertScaleAbs(sharpened1)
    sharpened2=cv2.convertScaleAbs(sharpened2)
    img_add=cv2.addWeighted(sharpened1,0.5,sharpened2,0.5,0)
    cv2.imshow("cam",img_add)
    if cv2.waitKey(10)==27:
        break
cap.release()
cv2.destroyAllWindows()
