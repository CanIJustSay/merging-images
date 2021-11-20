import cv2
image1 = cv2.imread("star1.jpg")
image2 = cv2.imread("diamond.jpg")

sub = cv2.subtract(image1, image2)

cv2.imshow("Subtraction", sub)
cv2.waitKey(0)