import cv2
import  numpy  as  np 
import time
t=str(int(time.time()))
def init(i):
    img = cv2.imread(i)
    size = img.shape
    X=[]
    Y=[]
    for x in range(size[0]):
        for y in range(size[1]):
            if img[x,y,0] > 100:
                X.append(y)
                Y.append(x)
    print(min(Y),max(Y),min(X),max(X))
    # 37:79,6:48 [y0:y1, x0:x1]
    cv2.imwrite('./seveimg/QK_seve'+t+'.png', img[min(Y)-5:max(Y)+5,min(X)-5:max(X)+5])
    return './seveimg/QK_seve'+t+'.png'