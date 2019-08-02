import cv2
import  numpy  as  np 
import tailor
import os
def init(QK, BG):
    # QK_min = './images/qk_min.png' #缺口小图片
    # QK = './images/qk.png' #缺口原始图片
    # BG = './images/bd.png' #背景图片

    newQKURL = tailor.init(QK) # 缺口原始图片的裁剪成下图片
    img = cv2.imread(newQKURL, 0) # 缺口原始图片
    os.remove(newQKURL) #删除图片
    yan = []
    size = img.shape
    retval, im_at_fixed = cv2.threshold(img, 35, 255, cv2.THRESH_BINARY) 
    for x in range(size[0]):
        for y in range(size[1]):
            if (y<size[1]-1) and (x<size[0]-1):
                if(im_at_fixed[x,y] != im_at_fixed[x,y+1]):
                    yan.append([x,y])
                if(im_at_fixed[x,y] != im_at_fixed[x+1,y]):
                    yan.append([x,y])
                if(im_at_fixed[x,y] != im_at_fixed[x+1,y+1]):
                    yan.append([x,y])

    X = []
    Y = []
    for list in yan:
        X.append(list[0])
        Y.append(list[1])

    emptyImage = np.zeros(size, np.uint8)	
    # print(yan)
    #显示图像 emptyImage
    for i in yan:
        emptyImage[i[0], i[1]] = 255

    #***********************************************
    am = cv2.imread(BG, 0)# 背景图片
    ret, im_at_fixed = cv2.threshold(am, 170, 255, cv2.THRESH_BINARY) 
    edges = cv2.Canny(im_at_fixed,100,200)



    result = cv2.matchTemplate(emptyImage, edges, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    aa = cv2.imread(BG) # 背景图片画出位置
    cv2.rectangle(aa, (y+4, x+4), (y+4 + max(Y)-min(Y), x+4 + max(X)-min(Y)), (255, 0, 0), 1)
    return y