import requests
import pageParse

r = requests.get('https://www.cnblogs.com/y896926473/p/6736722.html')
r.encoding = r.apparent_encoding
pageParse.parse(r.text)