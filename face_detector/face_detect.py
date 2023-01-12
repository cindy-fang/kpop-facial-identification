import cv2
import sys
import os
import pyautogui


# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(70, 70),
    flags = cv2.CASCADE_SCALE_IMAGE
)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 300, 0), 2)
    im = pyautogui.screenshot('test.png',region=(100,100,500,400))

cv2.imshow("Faces found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Found {0} faces!".format(len(faces)))

os.system("python face_search.py " + imagePath) 
# import PIL.ImageGrab
# screenshot = PIL.ImageGrab.grab()
# screenshot.show()