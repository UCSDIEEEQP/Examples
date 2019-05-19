import cv2 
import imutils 
#load image into a variable called image
image = cv2.imread('qp.JPG') 
#resizes image to 900 pixels wide
image = imutils.resize(image, 900) 
#places circle on image
cv2.circle(image, (100,100), 25, (0,255,0), 10) 
#places rectangle on image
cv2.rectangle(image, (400,300), (500,400), (0,0,255), 10) 
#creates font object for sans serif
font = cv2.FONT_HERSHEY_DUPLEX
#places text on image
cv2.putText(image, "Quarterly projects is the best", (200, 200), font, 1.0, (255, 255, 255), 1) 
#shows final image to our screen
cv2.imshow("window", image) 
#waits until key press
cv2.waitKey(0) & 0xFF
#closes all windows
cv2.destroyAllWindows() 