import cv2
import random


img = cv2.imread('assets/logo.png', -1)

print(type(img))
print(img)
print(img.shape) # Height, Width, Channels (BGR)

# Editing pixels

"""
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
"""
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

tag = img[250:350, 250:350]
img[300:400, 200:300] = tag

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()