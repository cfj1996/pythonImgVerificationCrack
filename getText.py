from bs4 import BeautifulSoup
import re



def get(html):
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find(id='cnblogs_post_body')
    text = tag.text
    t = re.findall(r'^\d+.*?$', text, flags=re.DOTALL+re.MULTILINE)
    for i in t:
        print(i)
