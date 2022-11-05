"""
使用多线程爬取文章内容
"""
import os.path
import requests
from bs4 import BeautifulSoup
import threading


# 获取文章内容
def get_page_content(soup):
    title = soup.h1
    text = soup.find(id="TextContent").find_all('p')[:-2]
    return [title, text]


# 保存html
def save_file(content, num):
    title = content[0]
    path = "book/"
    filename = os.path.join(path, '{:0>4d}'.format(num) + title.text + '.txt')
    with open(filename, mode='wt', encoding='utf-8') as f:
        for c in content[1]:
            f.write(c.text + "\n")
    print('{}保存完成！'.format(filename))


# 获取页面html
def get_html(page_url):
    html = requests.get(page_url).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


# 获取全部章节URL
def get_all_chapter(soup):
    a_lis = soup.find(id="chapterList").find_all('a')
    c_lis = []
    for li in a_lis:
        c_lis.append(li['href'])
    return c_lis


def main(curl, num):
    soup = get_html(curl)
    save_file(get_page_content(soup), num)


if __name__ == '__main__':
    start_url = 'https://www.23qb.com/book/51541/'
    domain_url = 'https://www.23qb.com'
    res = get_all_chapter(get_html(start_url))

    for index, url in enumerate(res, start=1):
        url = domain_url + url
        t = threading.Thread(target=main, args=(url, index))
        t.start()

