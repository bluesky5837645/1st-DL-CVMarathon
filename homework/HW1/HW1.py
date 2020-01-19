# example01
# import cv2
# ima=cv2.imread('lena.png')
# print(type(ima))
# cv2.imshow('BGR',ima)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#homework01
# import cv2
# ima=cv2.imread('Part01/lena.png')
# (R,G,B)=cv2.split(ima)
# cv2.imshow('r',R)
# cv2.imshow('g',G)
# cv2.imshow('b',B)
# cv2.waitKey(0)

##answer
import cv2
import numpy as np

# 以彩色圖片的方式載入
img = cv2.imread('Part01/lena.png', cv2.IMREAD_COLOR)

# 把圖片合併起來方便一起看
img_concat = np.hstack((img[:, :, 0], img[:, :, 1], img[:, :, 2]))

# 為了要不斷顯示圖片，所以使用一個迴圈
while True:
    # 顯示彩圖
    cv2.imshow('bgr', img)
    cv2.imshow('bgr_split', img_concat)
    
    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
