import requests
import pageParse
import getText

r = requests.get('https://www.cnblogs.com/sunmyboke/p/10364507.html')
r.encoding = r.apparent_encoding
# pageParse.parse(r.text)
getText.get(r.text)