import cv2
import os
os.system("cls")
readImage = cv2.imread("AnotherOne.jpg")
startPoint = (0,0)
endPoint = (200,200)
thickness = 9
color = (0,255,0)
newImage = cv2.arrowedLine(readImage,startPoint,endPoint,color,thickness)

cv2.imwrite("NewImage.png",newImage)
cv2.waitKey(0)