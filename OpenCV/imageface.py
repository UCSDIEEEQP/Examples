import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# grab the reference to the webcam
image = cv2.imread('qp.JPG')

faces = faceCascade.detectMultiScale(image)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,0,255), 20)
image_resize = cv2.resize(image, (1600,900))
# show the frame to our screen
cv2.imshow("Faces", image_resize)
#writes the image to the current directory
cv2.imwrite("faces.jpg", image_resize)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()