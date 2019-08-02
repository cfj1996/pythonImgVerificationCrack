# 操作dom
import random
def init(ActionChains,driver, L):
    slideblock = driver.find_element_by_class_name('geetest_slider_button')  #获取圆球
    ActionChains(driver).click_and_hold(slideblock).perform() #按下圆球
    ActionChains(driver).move_by_offset(xoffset=L,yoffset=0).perform() #拖动圆球    
    ActionChains(driver).pause(random.randint(6,14)/10).release(slideblock).perform() #放开圆球