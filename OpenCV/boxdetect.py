import numpy as np
import cv2
import imutils

#creates boundaries for the color red
boundaries = ([17, 17, 150], [50, 50, 255])
#places these boundaries into a numpy array
lower = np.array(boundaries[0], dtype = "uint8")
upper = np.array(boundaries[1], dtype = "uint8")
#creates a reference to the video source
vs = cv2.VideoCapture(0)
# keep looping
while True:
    # grab the current frame
    ret, frame = vs.read()
    #blurs the current frame
    frame = cv2.GaussianBlur(frame, (11, 11), 0)
    #remove all pixels that arent in the frame
    mask = cv2.inRange(frame, lower, upper)
    #remove small areas of pixels within the frame
    mask = cv2.erode(mask, None, iterations=2)
    #enlarges the remaining shapes
    mask = cv2.dilate(mask, None, iterations=2)
    #finds the countours in the mask
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

	# only proceed if at least one contour was found
    if len(contours) > 0:
        contour = max(contours, key=cv2.contourArea)
        #cv2.drawContours(frame, contour, -1, (0,255,0), 3)
        #draws a rectangle around the contours found
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame,[box],0,(0,0,255),2)
    #show image on screen    
    cv2.imshow("Object detection is awesome!", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
# close all windows
cv2.destroyAllWindows()