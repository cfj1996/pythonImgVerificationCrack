import cv2
import  numpy  as  np 

QK_min = './images/qk_min.png'
BG = './images/bd.png'
img = cv2.imread(QK_min, 0) # 缺口原始图片
yan = []
size = img.shape
retval, im_at_fixed = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY) 
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
aa = cv2.imread(BG) # 背景图片
cv2.rectangle(aa, (y+8, x+8), (y+8 + max(Y)-min(Y), x+8 + max(X)-min(Y)), (255, 0, 0), 1)
print('平移', y)
cv2.imshow('img', aa) 
cv2.waitKey(0)
cv2.destroyAllWindows()