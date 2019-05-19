import cv2
# grab the reference to the webcam
vs = cv2.VideoCapture(0)
# keep looping
while True:
	# grab the current frame
	ret, frame = vs.read()

	cv2.imshow("Webcam preview", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
# close all windows
cv2.destroyAllWindows()