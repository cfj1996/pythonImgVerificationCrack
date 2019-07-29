from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time,random
# import cv2
import re
import json
import os
import requests
import time
import base64
import range
t = str(int(time.time()))
os.makedirs('./downloadimg/', exist_ok=True)
URL = "https://zzk.cnblogs.com/s?t=b&w=%E5%89%8D%E7%AB%AF%E9%9D%A2%E8%AF%95%E9%A2%98"
driver = webdriver.Chrome()
driver.get(URL)

# 下载小缺口的Canvas图片 
time.sleep(5)
QK_src = './downloadimg/'+t+'QK.png'
getQKImgJS = 'return document.getElementsByClassName("geetest_canvas_slice")[0].toDataURL("image/png");'
QK_img = driver.execute_script(getQKImgJS)
QK_img = QK_img[QK_img.find(',') + 1:]
img_QK_data = base64.b64decode(QK_img)
file_QK = open(QK_src, 'wb')
file_QK.write(img_QK_data)
file_QK.close()

# 下载Canvas背景图
BG_src = './downloadimg/'+t+'bg.png'
getImgJS = 'return document.getElementsByClassName("geetest_canvas_bg")[0].toDataURL("image/png");'
bg_img = driver.execute_script(getImgJS)
bg_img = bg_img[bg_img.find(',') + 1:]
img_data = base64.b64decode(bg_img)
file = open(BG_src, 'wb')
file.write(img_data)
file.close()
L = range.init(QK_src, BG_src)
# 删除下载的图片
os.remove(QK_src)
os.remove(BG_src)
# print('平移距离',L) 

# geetest_slider_button geetest_refresh_1 geetest_canvas_bg dom 鼠标拖动运动
slideblock = driver.find_element_by_class_name('geetest_slider_button')  #获取圆球
ActionChains(driver).click_and_hold(slideblock).perform() #按下圆球
ActionChains(driver).move_by_offset(xoffset=L,yoffset=0).perform() #拖动圆球
ActionChains(driver).pause(random.randint(6,14)/10).release(slideblock).perform() #放开圆球
time.sleep(10)
driver.close()