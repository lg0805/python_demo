# @FileName : python实现生产者消费者爬虫
# @Time     : 2022/11/5 20:48
# @Author   : ligg

import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50 + 1)
]


# 获取页面HTML
def craw(url):
    r = requests.get(url)
    return r.text


# 解析页面
def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='post-item-title')
    return [(link["href"], link.get_text()) for link in links]


if __name__ == '__main__':
    for result in parse(craw(urls[2])):
        print(result)