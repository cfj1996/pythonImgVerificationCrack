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
os.makedirs('./image/', exist_ok=True)



driver = webdriver.Chrome()
driver.get('https://zzk.cnblogs.com/s?t=b&w=%E9%9D%A2%E8%AF%95%E9%A2%98')

# geetest_slider_button geetest_refresh_1 geetest_canvas_bg
time.sleep(3)
load = driver.find_element_by_class_name('geetest_refresh_1')  #获取圆球
actions = ActionChains(driver).click(load).perform() # 刷新图片


# 拖到
time.sleep(2)
slideblock = driver.find_element_by_class_name('geetest_slider_button')  #获取圆球
ActionChains(driver).click_and_hold(slideblock).perform() #按下圆球
ActionChains(driver).move_by_offset(xoffset=160,yoffset=0).perform() #拖动圆球
ActionChains(driver).pause(random.randint(6,14)/10).release(slideblock).perform() #放开圆球

# 获取请求小图片的地址
script = driver.find_elements_by_tag_name('script')
for i in script:
    if i.get_attribute('src').find('/refresh.php?gt') != -1:
        imgUrl = i.get_attribute('src')
# 请求地址
imgdriver = webdriver.Chrome()
imgdriver.get(imgUrl)
text = imgdriver.find_element_by_tag_name('pre').text
imgdriver.close()
key = text.find('({')
jsonStr = text[key+1:len(text)-1]
val =json.loads(jsonStr)

# 下载小缺口图片
imgName = './image/'+str(time.time())+ '.png'
imgSrc = "https://static.geetest.com/" + val['slice']
print(imgSrc)
r = requests.get(imgSrc, stream=True)    
with open(imgName, 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)

# 保存背景图
time.sleep(2)
getImgJS = 'return document.getElementsByClassName("geetest_canvas_bg")[0].toDataURL("image/png");'
bg_img = driver.execute_script(getImgJS)
bg_img = bg_img[bg_img.find(',') + 1:]
img_data = base64.b64decode(bg_img)
file = open('./image/'+str(time.time())+'bg.png', 'wb')
file.write(img_data)
file.close()

# 显示图片
# time.sleep(3)
# img = cv2.imread(imgName)
# cv2.namedWindow("Image") 
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# def get_track(self,distance):
#     track=[]
#     current=0
#     mid=distance*3/4
#     t=random.randint(2,3)/10
#     v=0
#     while current<distance:
#           if current<mid:
#              a=2
#           else:
#              a=-3
#           v0=v
#           v=v0+a*t
#           move=v0*t+1/2*a*t*t
#           current+=move
#           track.append(round(move))
#     return track
# # 生成拖拽移动轨迹，加3是为了模拟滑过缺口位置后返回缺口的情况
# track_list=get_track(127+3)
# time.sleep(2)
# ActionChains(driver).click_and_hold(slideblock).perform()
# time.sleep(0.2)
# # 根据轨迹拖拽圆球
# for track in track_list:
#     ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
# # 模拟人工滑动超过缺口位置返回至缺口的情况，数据来源于人工滑动轨迹，同时还加入了随机数，都是为了更贴近人工滑动轨迹
# imitate=ActionChains(driver).move_by_offset(xoffset=-1, yoffset=0)
# time.sleep(0.015)
# imitate.perform()
# time.sleep(random.randint(6,10)/10)
# imitate.perform()
# time.sleep(0.04)
# imitate.perform()
# time.sleep(0.012)
# imitate.perform()
# time.sleep(0.019)
# imitate.perform()
# time.sleep(0.033)
# ActionChains(driver).move_by_offset(xoffset=1, yoffset=0).perform()
# # 放开圆球
# ActionChains(driver).pause(random.randint(6,14)/10).release(slideblock).perform()
# time.sleep(2)
# #务必记得加入quit()或close()结束进程，不断测试电脑只会卡卡西
# driver.close()