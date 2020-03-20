from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import setdom
import time
import random
driver = webdriver.Chrome()
driver.get('https://mp.dayu.com/')
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
left = [1, 4, 7, 10, 15, 22, 30, 37, 44, 51, 57, 61, 63, 65, 68, 72, 76, 80, 84, 88, 92, 96, 100, 105, 109, 112, 115, 120, 127, 133, 138, 144, 149, 154, 159, 164, 169, 173, 176, 179, 184, 188,192,200]

try:  # 判断图片滑动是否加载
    isload = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nc_1_n1z"))
    )
except:
    print('\033[1;35m nc_1_n1z未加载 \033[0m')
    driver.close()
finally:
    time.sleep(3)
    slideblock = driver.find_element_by_id('nc_1_n1z')  #获取圆球
    ActionChains(driver).click_and_hold(slideblock).perform() #按下圆球
    for i in left:
        time.sleep(0.02)
        ActionChains(driver).move_by_offset(xoffset=i,yoffset=0).perform() #拖动圆球  
    ActionChains(driver).pause(random.randint(6,14)/10).release(slideblock).perform() #放开圆球
