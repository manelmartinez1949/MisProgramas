##Captura de VIDEO
import cv2
camera=cv2.VideoCapture(0)
while True:
    ret, frame=camera.read()
    cv2.imshow("Security Camera", frame)
    if cv2.waitkey(1)and 0xFF==ord('q'):
               break
camera.release()
cv2.destryAllWindows()
