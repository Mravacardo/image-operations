import cv2
import numpy as np

img=cv2.imread("Bird.png", 0)
cv2.imshow("Bird.png", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img1=cv2.imread("two dots.jpg")
# img2=cv2.imread("one dot.png")
# wait1=cv2.addWeighted(img1, 0.5, img2, 0.4, 1.5)
# wait2=cv2.addWeighted(img1, 0.5, img2, 0.4, 0)
# cv2.imshow("two dots", img1)
# cv2.imshow("one dot", img2)
# cv2.imshow("bright", wait1)
# cv2.imshow("dull", wait2)
# #subtracting image
# subtracted=cv2.subtract(wait1, img1)
# cv2.imshow("subtracted", subtracted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img3=cv2.resize(img,(200, 200))
# cv2.imshow("Resized bird.png", img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# kernel = np.ones((20, 20), np.uint8)

# img4 = cv2.erode(img, kernel)
# cv2.imshow("Eroded Image", img4)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Gaussian = cv2.GaussianBlur(img, (15, 15), 0)
# cv2.imshow('Gaussian Blurring', Gaussian)
# cv2.waitKey(0)

# median = cv2.medianBlur(img, 15)
# cv2.imshow('Median Blurring', median)
# cv2.waitKey(0)

# bilateral = cv2.bilateralFilter(img, 9, 75, 75)
# cv2.imshow('Bilateral Blurring', bilateral)
# cv2.waitKey(0)

#cv2.destroyAllWindows()

# borderedImage = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT, value = 1)

# cv2.imshow("Bordered Image", borderedImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
