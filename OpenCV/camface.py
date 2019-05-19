import cv2

#import the trained classifier for the facial detection
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
#creates a font object
font = cv2.FONT_HERSHEY_DUPLEX
# grab the reference to the webcam
vs = cv2.VideoCapture(0)

# keep looping
while True:
	# grab the current frame
	ret, frame = vs.read()
  
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
	faces = faceCascade.detectMultiScale(frame) #gets faces from frame
	for (x, y, w, h) in faces: #goes across all faces in image
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2) #places a rectangle around the face
		cv2.putText(frame, "Face", (x + 6, y+h - 6), font, 1.0, (255, 255, 255), 1) #puts text next to face
	# show the frame to our screen
	cv2.imshow("Video", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
 
# close all windows
cv2.destroyAllWindows()