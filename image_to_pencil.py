import cv2

fpath = 'puppy.jpg'

img = cv2.imread(fpath)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray = 255 - gray
blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
inverted_blurred = 255 - blurred

pencil_sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

cv2.imshow('Original image', img)
cv2.imshow('New image', pencil_sketch)
cv2.waitKey(0)
