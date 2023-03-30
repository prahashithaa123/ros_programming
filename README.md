# ros_programming

#Drowsiness Detection Tutorial.ipynb
#https://github.com/nicknochnack/YOLO-Drowsiness-Detection/blob/main/Drowsiness%20Detection%20Tutorial.ipynb

#haar caascade
#xml file creation
#https://amin-ahmadi.com/cascade-trainer-gui/

#code - import cv2
# Load the cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Read the input image
frameWidth = 480
frameHeight = 480
img = cv2.imread("Trumps.jpg")
# Convert into grayscale
img=cv2.resize(img, (frameWidth, frameHeight))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
cv2.imshow("img", img)
cv2.waitKey(0)



