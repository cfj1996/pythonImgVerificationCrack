# 下载图片
import base64
import time
import os
import random
def init(driver, dom):
    t = str(int(time.time()+random.randint(0, 1000000)))
    imgsrc = './downloadimg/'+dom+t+'.png'
    getQKImgJS = 'return document.getElementsByClassName("'+dom+'")[0].toDataURL("image/png");'
    QK_img = driver.execute_script(getQKImgJS)
    QK_img = QK_img[QK_img.find(',') + 1:]
    img_QK_data = base64.b64decode(QK_img)
    file_QK = open(imgsrc, 'wb')
    file_QK.write(img_QK_data)
    file_QK.close()
    return imgsrc
