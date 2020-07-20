import  cv2
import numpy as np

img_path="lena.png"
# 以彩色圖片的方式載入
img=cv2.imread('lena.png',cv2.IMREAD_COLOR)
# 為了要改變飽和度，我們先把 color space 轉成 HSV 格式
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
Change_percnetage=0.2
# 針對飽和度的值做改變，超過界線 0~1 的都會 bound
# 在 HSV color space 減少飽和度
img_hsv_down=img_hsv.astype("float32")
img_hsv_down[:,:,1]=img_hsv_down[:,:,1]/255-Change_percnetage
img_hsv_down[:,:,1][img_hsv_down[:,:,1]<0]=0
img_hsv_down[:,:,1]=img_hsv_down[:,:,1]*255
img_hsv_down=img_hsv_down.astype("uint8")
# 轉換
img_hsv_down=cv2.cvtColor(img_hsv_down,cv2.COLOR_HSV2BGR)
# 在 HSV color space 增加飽和度
img_hsv_up=img_hsv.astype("float32")
img_hsv_up[:,:,1]=img_hsv_up[:,:,1]/255+Change_percnetage
img_hsv_up[:,:,1][img_hsv_up[:,:,1]>0]=1
img_hsv_up[:,:,1]=img_hsv_up[:,:,1]*255
img_hsv_up=img_hsv_up.astype("uint8")
# 轉換
img_hsv_up=cv2.cvtColor(img_hsv_up,cv2.COLOR_HSV2BGR)
# 組合圖片 + 顯示圖片
img_hsv_change=np.hstack((img,img_hsv_down,img_hsv_up))
while True:
    cv2.imshow("change saturation",img_hsv_change)
    k=cv2.waitKey(0)
    if k==ord("e"):
        cv2.destroyAllWindows()
        break
k=0
# case 1
# 每個 channel 個別做直方圖均衡
img_bgr_equal = img.copy()
img_bgr_equal[...,0]=cv2.equalizeHist(img[...,0])
img_bgr_equal[...,1]=cv2.equalizeHist(img[...,1])
img_bgr_equal[...,2]=cv2.equalizeHist(img[...,2])
# case 2 - 轉換 color space 後只對其中一個 channel 做直方圖均衡
img_hsv_equal=img_hsv.copy()
img_hsv_equal[...,2] = cv2.equalizeHist(img_hsv[...,2])
img_hsv_equal=cv2.cvtColor(img_hsv_equal,cv2.COLOR_HSV2BGR)
# 比較 (原圖, BGR color space 對每個 channel 做直方圖均衡, HSV color space 對明度做直方圖均衡)
img_bgr_equalHist = np.hstack((img, img_bgr_equal, img_hsv_equal))
while True:
    cv2.imshow("bgr equal histogram",img_bgr_equalHist)
    k=cv2.waitKey(0)
    if k==ord('e'):
        cv2.destroyAllWindows()
        break
k=0
# alpha: 控制對比度 (1.0~3.0)
# beta: 控制明亮度 (0~255)
add_contrast = cv2.convertScaleAbs(img,alpha=2.0,beta=0)
add_lighness = cv2.convertScaleAbs(img,alpha=1,beta=50)

img_contrast_light=np.hstack((img,add_contrast,add_lighness))
while True:
    cv2.imshow("adjust contrast and brighness",img_contrast_light)
    k=cv2.waitKey(0)
    if k==ord('e'):
        cv2.destroyAllWindows()
        break












