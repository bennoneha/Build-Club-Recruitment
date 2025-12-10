import cv2
path=r"C:\Users\neha0\Downloads\Passport size Neha.jpg"
image=cv2.imread(path)
imginvert=255-image

imagegray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invertgray=255-imagegray
gaussianblur=cv2.GaussianBlur(invertgray,(91,91),0)
invertgaussianblur=255-gaussianblur
sketch=cv2.divide(imagegray,invertgaussianblur,scale=265.0)

cv2.imshow("Image",image)
cv2.imshow("invert",imginvert)
cv2.imshow("gray",imagegray)
cv2.imshow("invertgray",invertgray)
cv2.imshow("gaussianblur",gaussianblur)
cv2.imshow("invertgaussianblur",invertgaussianblur)
cv2.imshow("sketch",sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()

