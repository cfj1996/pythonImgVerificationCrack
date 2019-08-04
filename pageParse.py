from bs4 import BeautifulSoup
import re


def isCli(dom):
    try:
        if(dom.parent['id'] == 'cnblogs_post_body'):
            return dom
    except:
        return isCli(dom.parent)


def parse(text):
    newtext = re.sub(r'\n|\r', '', text)
    soup = BeautifulSoup(newtext, 'html.parser', from_encoding="utf-8")
    reg = re.compile('^\d+()\D')
    topic = []  # 题
    children = []
    DATA = []

    tag = soup.find_all(text=reg)
    for i in tag:
        topic.append(isCli(i.parent))
    for chil in soup.find(id='cnblogs_post_body').children:
        children.append(chil)

    data = []
    for key in range(len(topic)):
        try:
            key1 = topic[key]
            key2 = topic[key+1]
            index1 = children.index(key1)
            index2 = children.index(key2)
            data.append(
                {"T": tag[key].string, "D": children[index1:index2]})
        except:
            #     data.append({"T":topic[t].string,"D":children[key:len(topic)]})
            data.append(
                {"T": tag[key].string, "D": children[index1:len(children)]})
    xb = []
    if(len(data)>10):
        data.pop()
    for i in range(len(data)):
        key = (re.compile(r'^\d+').match(data[i]["T"])).group(0)  # 当前的题目的序号
        if(key == '1'):
            xb.append(i)
    xb.append(len(data))
    print(xb)
    for i in range(len(xb)):
        if(i > 0 and xb[i]-xb[i-1] < 4):
                for key in range(xb[i-1], xb[i]):
                        # print(data[key])
                        data.remove(data[xb[i-1]])


    for i in data:
        tag = soup.find_all(text=i['T'])[0].parent
        i['T'] = re.sub(r'^[1-9](\.|[0-9])', '', str(i['T']))
        text = ''
        for d in i["D"]:
                if(d.string != ''):
                        text += re.sub(re.escape(str(tag)), '', str(d))
        i["D"] = text


    for i in data:
        print(i)
        print('\033[1;35m **************** \033[0m')
