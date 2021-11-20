import cv2
import os 
os.system("cls")
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")

mergeImage = cv2.addWeighted(image1,0.5,image2,0.5,0)

names = ["image4.png","image5.png"]

for i in names:
    img = cv2.imread(i)
    mergeImage = cv2.addWeighted(img,0.3,mergeImage,0.7,0)

cv2.imshow("mergeImage",mergeImage)

cv2.waitKey(0)
#cv2.imwrite("newImage.jpg",mergeImage)
