import cv2
import  numpy  as  np 
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
    return img[min(Y)-1:max(Y)+3,min(X)-1:max(X)+3]