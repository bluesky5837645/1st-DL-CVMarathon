import cv2
import numpy as np

img_path = 'lena.png'
img = cv2.imread(img_path)
#矩形
img_rect= img.copy()
cv2.rectangle(img_rect,(60,40),(420,510),(0,0,255),3)
while True:
    cv2.imshow("image",img_rect)
    k=cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
        break
k=0
#線
img_line=img.copy()
cv2.line(img_line,(60,40),(420,510),(0,0,255),3)
while True:
    cv2.imshow("image",img_line)
    k=cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
        break
k=0
#文字
img_text=img.copy()
cv2.putText(img_text,"(60,40)",(60,40),0,1,(0,0,255),3)
while True:
    cv2.imshow("image",img_text)
    k=cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
        break
k=0
#解法二
# 對明亮度做直方圖均衡處理
# 水平鏡像 + 縮放處理 (0.5 倍)
# 畫出人物矩形邊框
#(有很多解法，有分成知道矩形座標的跟不知道的)
img_hw=img.copy()  #這邊其實也可以把鏡射矩陣包含到Transformatopn Matrix上面
point_1=[img.shape[1]-60,40]
point_2=[img.shape[1]-420,510]
point_1=np.array(point_1)
point_2=np.array(point_2)
img_hw=cv2.cvtColor(img_hw,cv2.COLOR_BGR2HSV)
img_hw[...,2]=cv2.equalizeHist(img_hw[...,2])
img_hw=cv2.cvtColor(img_hw,cv2.COLOR_HSV2BGR)
img_hw=img_hw[:,::-1,:]
#img_hw=cv2.resize(img_hw,None,fx=0.5,fy=0.5)
M_scale=np.array([
    [0.5,0,0],
    [0,0.5,0],
],dtype="float32")
img_hw=cv2.warpAffine(img_hw,M_scale,(int(img_hw.shape[0]*0.5),int(img_hw.shape[1]*0.5)))
new_point_1=np.dot(M_scale.T,point_1)
new_point_2=np.dot(M_scale.T,point_2)
new_point_1=new_point_1.astype("uint8")
new_point_2=new_point_2.astype("uint8")
print("The new_point_1 of the left up side is {}".format(new_point_1))
print("The new_point_1 of the right down side is {}".format(new_point_2))
cv2.rectangle(img_hw,tuple(new_point_1[0:2]),tuple(new_point_2[0:2]),(0,0,255),3)
while True:
    cv2.imshow("img_hw",img_hw)
    k=cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
        break

#解法三 (optional)

