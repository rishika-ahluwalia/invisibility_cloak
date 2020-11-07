import cv2


cap= cv2.VideoCapture(0)
while cap.isOpened():
    ret, back = cap.read()
    if ret == True:
        cv2.imshow("image",back)
        if cv2.waitKey(50) == ord('q'):
            #save the image
            cv2.imwrite('Resources/image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()