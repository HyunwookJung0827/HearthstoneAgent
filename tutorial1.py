import cv2

img = cv2.imread('assets/logo.png', -1) # directory and the mode of the media
img = cv2.resize(img, (400, 400))

# We loaded img with our image korea japan.png
cv2.imshow('Image', img) #'Image' is the name of our window showing image
cv2.waitKey(0) # How we close the window. 0 means any key, 5 means wait 5 seconds to close unless any key is pressed
cv2.destroyAllWindows()
