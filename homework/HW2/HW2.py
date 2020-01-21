#example
# import cv2
# img_path = 'Part01/lena.png'
# # 以彩色圖片的方式載入
# img = cv2.imread(img_path, cv2.IMREAD_COLOR)
# # 改變不同的 color space
# img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # 為了要不斷顯示圖片，所以使用一個迴圈
# while True:
#     cv2.imshow('bgr', img)
#     cv2.imshow('hsv', img_hsv)
#     # 直到按下 ESC 鍵才會自動關閉視窗結束程式
#     k = cv2.waitKey(0)
#     if k == 27:
#         cv2.destroyAllWindows()
#         break

#homework
import cv2
import numpy as np
ima=cv2.imread("Part01/lena.png",cv2.IMREAD_COLOR)
ima1=cv2.cvtColor(ima,cv2.COLOR_BGR2HSV)
ima2=cv2.cvtColor(ima,cv2.COLOR_BGR2HLS)
ima3=cv2.cvtColor(ima,cv2.COLOR_BGR2LAB)
array=np.hstack((ima,ima1,ima2,ima3))
cv2.imshow("change color",array)
cv2.waitKey(0)
cv2.destroyWindow()


