from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
import random
import re
import range
import dowimg
import setdom
import os
import uuid


def init(URL):
    driver = webdriver.Chrome()
    driver.get(URL)
    now = datetime.now()
    urlList = []
    try:  # 判断图片滑动是否加载
        isload = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "geetest_absolute"))
        )
    finally:
        time.sleep(1)  # 等待1s,图片加载完
        setdom.init(ActionChains, driver, 20)
        time.sleep(2)

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "searchURL"))
            )
        except:
            print('验证失败')
            driver.close()
        finally:
            try: 
                urldoms = driver.find_elements_by_class_name('searchURL')
                for i in urldoms:
                    urlList.append((str(uuid.uuid1()),i.text, now))
                driver.close()
                print('爬取成功', URL)
            except :
                urlList = []               
    return urlList
init('https://zzk.cnblogs.com/s/blogpost?Keywords=前端面试题&pageindex=1')