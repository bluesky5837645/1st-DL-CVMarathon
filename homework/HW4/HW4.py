import cv2
import numpy as np
import time

img_path='lena.png'
img=cv2.imread(img_path)
# 水平翻轉 (horizontal)
img_hflip = img.copy()
img_hflip=img_hflip[:,::-1,:]
# 垂直翻轉 (vertical
img_vflip = img.copy()
img_vflip =img[::-1,:,:]
# 水平 + 垂直翻轉
img_hvflip =img.copy()
img_hvflip=img_hvflip[::-1,::-1,:]
# 組合 + 顯示圖片
hflip=np.hstack((img,img_hflip))
vflip=np.hstack((img_vflip,img_hvflip))
img_flip=np.vstack((hflip,vflip))
while True:
    cv2.imshow('flip image',img_flip)
    k=cv2.waitKey(0)
    if k==ord("e"):
        cv2.destroyAllWindows()
        break
k=0
# 將圖片縮小成原本的 20% degault=cv2.INTER_LINEAR
img_test=cv2.resize(img,None,fx=0.2,fy=0.2)
# 將圖片放大為"小圖片"的 8 倍大 = 原圖的 1.6 倍大
img_test_2=cv2.resize(img_test,None,fx=8,fy=8)
# 鄰近差值 scale + 計算花費時間
start_time=time.time()
img_area_scale=cv2.resize(img_test,None,fx=8,fy=8,interpolation=cv2.INTER_NEAREST)
print('INTER_CUBIC zoom cost %s'% str(time.time()-start_time))
#print('INTER_NEAREST zoom cost {}'.format(time.time() - start_time))
# 組合 + 顯示圖片
orig_img=cv2.resize(img,img_area_scale.shape[0:2])
img_zoom=np.hstack((orig_img,img_area_scale))
while True:
    cv2.imshow("zoom image",img_zoom)
    k=cv2.waitKey(0)
    if k==ord("e"):
        cv2.destroyAllWindows()
        break
k=0
# 設定 translation transformation matrix
# x 平移 50 pixel; y 平移 100 pixel
M=np.array([
    [1,0,50],
    [0,1,100],
],dtype='float32')
shift_img=cv2.warpAffine(img,M,(img.shape[0],img.shape[1]))
# 組合 + 顯示圖片
img_shift = np.hstack((img, shift_img))
while True:
    cv2.imshow('shift image',img_shift)
    k=cv2.waitKey(0)
    if k==ord("e"):
        cv2.destroyAllWindows()
        break








