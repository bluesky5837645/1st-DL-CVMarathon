# example01
# import cv2
# ima=cv2.imread('lena.png')
# print(type(ima))
# cv2.imshow('BGR',ima)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#homework01
import cv2
ima=cv2.imread('Part01/lena.png')
(R,G,B)=cv2.split(ima)
cv2.imshow('r',R)
cv2.imshow('g',G)
cv2.imshow('b',B)
cv2.waitKey(0)

