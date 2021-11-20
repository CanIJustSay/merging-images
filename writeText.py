import cv2

readImage = cv2.imread("AnotherOne.jpg")
font = cv2.FONT_HERSHEY_COMPLEX
org = (50,50)
fontScale = 1
color = (255,0,0)
thickness = 2
newImage = cv2.putText(readImage,"Hello",org,font,fontScale,color,thickness,cv2.LINE_AA)
cv2.imwrite("writtenImg.png",newImage)
