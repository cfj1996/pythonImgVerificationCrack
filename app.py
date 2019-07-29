import cv2
import  numpy  as  np 
import tailor
QK = './images/qk.png'
print(tailor.init(QK).shape)
cv2.imshow('img', tailor.init(QK)) 
cv2.waitKey(0)
cv2.destroyAllWindows()
