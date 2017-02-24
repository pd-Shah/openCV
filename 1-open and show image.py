import numpy as np
import cv2

print(cv2.__version__)


## Load an color image in grayscale
##cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
##cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
##cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)
print("img",img)
print("img.shape",img.shape)



#Display an image
cv2.imshow('image',img)

##cv2.waitKey() is a keyboard binding function.
##Its argument is the time in milliseconds.
##The function waits for specified milliseconds for any keyboard event.
##If you press any key in that time, the program continues.
##If 0 is passed, it waits indefinitely for a key stroke.
#It can also be set to detect specific key strokes like,
##if key a is pressed etc which we will discuss below.
cv2.waitKey(0)



##cv2.destroyAllWindows() simply destroys all the windows
##we created. If you want to destroy any specific window,
##use the function
##cv2.destroyWindow() where you pass the exact window name
##as the argument.
cv2.destroyAllWindows()


##
## you can already create a window and
## load image to it later.
cv2.namedWindow('1', cv2.WINDOW_NORMAL)
cv2.imshow('1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##Write an image
##Use the function cv2.imwrite() to save an image.
##First argument is the file name,
##second argument is the image you want to save.
cv2.imwrite('messigray.png',img)
