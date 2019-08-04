# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
newtext = "<p><strong>15.JavaScript原型，原型链 ? 有什么特点？</strong><br/>（1）原型对象也是普通的对象，是对象一个自带隐式的 __proto__ 属性，原型也有可能有自己的原型，如果一个原型对象的原型不为null的话，我们就称之为原型链。<br/>（2）原型链是由一些用来继承和共享属性的对象组成的（有限的）对象链。</p>"
soup  = BeautifulSoup(newtext,'html.parser', from_encoding="utf-8")
list = soup.find()
tag = soup.find_all(text='15.JavaScript原型，原型链 ? 有什么特点？')[0].parent
text = re.sub(re.escape('<strong>15.JavaScript原型，原型链 ? 有什么特点？</strong>'), '', newtext)
print(text)
for i in list:
    print(i)
    print('\033[1;35m ```````````````````````````````` \033[0m')
