import requests
import pageParse

r = requests.get('https://www.cnblogs.com/yuqingfamily/p/6866163.html')
r.encoding = r.apparent_encoding
JQ = pageParse.parse(r.text)
print(JQ)