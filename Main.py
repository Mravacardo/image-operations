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

# img5 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV )
# cv2.imshow("original", image)
# cv2.imshow("weird colour", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# edges = cv2.Canny(img, 10, 20)

# cv2.imshow('Original Image', img)
# cv2.imshow('Edged Image', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# rows, cols,_ = img.shape

# M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -65, 1)
# res = cv2.warpAffine(img, M, (cols, rows))

# result = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imshow('result', result)
# cv2.imshow('Original image', img)
# cv2.imshow('Rotated Image', res)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# (row, col) = img.shape[0:2]

# for i in range(row):
#     for j in range(col):
#         img[i, j] = sum(img[i, j]) * 1

# cv2.imshow('Grayscale Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

img = cv2.imread('eagle .jpg')

# start_point = (0, 50)

# end_point = (100, 50)

# colour = (235, 124, 243)

# thickness = 15

# cv2.imshow('original', img)

# img1 = cv2.line(img, start_point, end_point, colour, thickness)

# cv2.imshow('line image', img1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# rectangle drawing

# start_point = (100, 50)

# end_point = (400, 450)

# colour = (235, 124, 243)

# thickness: - = filled, + = outline

# thickness = -1

# cv2.imshow('original', img)

# img1 = cv2.rectangle(img, start_point, end_point, colour, thickness)

# cv2.imshow('rectangle image', img1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# circle drawing

# centre_point = (300, 200)

# radius = (60)

# colour = (235, 124, 243)

# thickness = -1

# cv2.imshow('original', img)

# img1 = cv2.circle(img, centre_point, radius, colour, thickness)

# cv2.imshow('circle image', img1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# text

# origin = (130, 240)

# font = cv2.FONT_HERSHEY_COMPLEX

# font_scale = 1.5

# colour = (231, 142, 132)

# thickness = 5

# cv2.imshow('original', img)

# img1 = cv2.putText(img, "Hello World", origin, font, font_scale, colour, thickness, cv2.LINE_AA)

# cv2.imshow('text image', img1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import numpy as np

# img = cv2.imread("blobby circles.jpg", cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray_blurred = cv2.blur(gray, (3,3))

# detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 20, param2 = 10, minRadius = 1, maxRadius = 20)

# if detected_circles is not None:
#     detected_circles = np.uint16(np.around(detected_circles))
#     for pt in detected_circles[0, :] :
#         a, b, r = pt[0], pt[1], pt[2]
#         cv2.circle(img, (a,b), r, (0, 255, 0), 2)
#         cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
#         cv2.imshow("Detected Circles", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
