import re
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://www.jikexueyuan.com/'
    r = requests.get(url)
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    i = 1
    for link in soup.find_all('a', 'card'):
        demo = str(link.contents)
        pattern = re.findall('src="(.*?)"', demo)  # 这是一个list,但是只有一个字符串
        html = pattern[0]  # 把list中的字符串提取出来
        print('now downloading the ' + str(i) + ' picture')
        with open('pic//' + str(i) + '.png', 'wb') as f:
            f.write(requests.get(html).content)  # 注意这里是content
        i += 1
