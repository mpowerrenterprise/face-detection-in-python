import cv2

faceModel = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")

video = cv2.VideoCapture("test-video.mp4")

while True:

	ret,frame = video.read()

	if ret == False:
		break

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	faces = faceModel.detectMultiScale(gray,1.3,5)

	for(x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

	cv2.imshow("Display", frame)

	if(cv2.waitKey(1) == ord("q")):
		break


video.release()
cv2.destroyAllWindows()


