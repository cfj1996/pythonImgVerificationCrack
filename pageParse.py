
from bs4 import BeautifulSoup
import re
def isCli(dom):
    try: 
        print(dom.parent['id'] == 'cnblogs_post_body')
        if(dom.parent['id'] == 'cnblogs_post_body'):
            return dom.parent
    except:
       return isCli(dom.parent)




def parse(text):
    newtext = re.sub(r'\n|\r','',text)
    soup  = BeautifulSoup(newtext,'html.parser', from_encoding="utf-8")
    reg = re.compile('^[1-9](\.|[0-9])\D')
    topic = []
    children = []
    tag = soup.find_all(text=reg)
    for i in tag:
        topic.append(isCli(i.parent))
    print(topic)
    for chil in soup.find(id='cnblogs_post_body').children:
       children.append(chil)

 
    for t in enumerate[topic]:
        try: 
            key1 = topic[t]
            key2 = topic[t+1]
            index = children.index(key2)
        except:
            key1 = topic[t] 
            
        print(index)
