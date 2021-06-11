import cv2 as cv

img = cv.imread("rs.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_gr_inv = 255 - img_gray
img_blur = cv.GaussianBlur(img_gr_inv,ksize=(21,21),sigmaX=0,sigmaY=0)

def dodgeV2(image,mask):
    return (cv.divide(image, 255 - mask, scale = 256))

def burnV2(image, mask):
    return (255 - cv.divide(255 - image, 255 - mask, scale=256))

img_blend = dodgeV2(img_gray, img_blur)

cv.imwrite('result.jpg',img_blend)

cv.imshow("gray.jpg",img_blend)
cv.waitKey(0)
