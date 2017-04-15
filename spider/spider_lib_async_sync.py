# -*- coding: utf-8 -*-

import time
import gzip
import aiohttp
import asyncio
from bs4 import BeautifulSoup

import urllib.request
from collections import deque

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/54.0.2840.71 Safari/537.36',
           'Accept-Encoding': 'gzip',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Accept': 'text/html,application/xhtml+xml,application/xml;'
                     'q=0.9,image/webp,*/*;q=0.8'}

def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all('a', {'class': 'contentHerf'})


# ------------------- 异步方式 ---------------------

# 已爬段子
ASYNC_CONTENT_QUEUE = asyncio.Queue()


async def async_qiubai(base_url):
    session = aiohttp.ClientSession()
    try:
        for page in range(1, 36):
            url = base_url.format('/text/page/' + str(page))
            # print('获取url: {}'.format(url))
            html = await async_get_html(session, url)
            await asyncio.sleep(0.5)
            await async_get_content(html)
    except Exception as e:
        print(e)
    finally:
        session.close()


async def async_get_html(session, url):
    resp = await session.get(url, headers=HEADERS)
    # print(resp.text())
    return await resp.text()


async def async_get_content(html):
    all_link = get_links(html)
    # print("本页面共有 {} 条段子".format(len(all_link)))
    for link in all_link:
        content = link.find('span')
        if content:
            await ASYNC_CONTENT_QUEUE.put(content.text)


# -------------------------------------------------

# ------------------- 同步方式 ---------------------

# 已爬段子
SYNC_CONTENT_QUEUE = deque()


def sync_qiubai(base_url):
    try:
        for page in range(1, 36):
            url = base_url.format('/text/page/' + str(page))
            html = sync_get_html(url)
            sync_get_content(html)
            time.sleep(0.5)
    except Exception as e:
        print(e)


def sync_get_html(url):
    req = urllib.request.Request(url=url,
                                 headers=HEADERS)
    response = urllib.request.urlopen(req)
    gzip_file = gzip.GzipFile(fileobj=response)
    html = gzip_file.read()
    return html


def sync_get_content(html):
    all_link = get_links(html)
    for link in all_link:
        content = link.find('span')
        if content:
            SYNC_CONTENT_QUEUE.append(content.text)


# -------------------------------------------------


def main():
    base_url = 'http://www.qiushibaike.com{}'
    async_start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_qiubai(base_url))
    loop.close()
    print('异步爬虫抓取 {number} 条段子， 用时 {time}'.format(number=ASYNC_CONTENT_QUEUE.qsize(),
                                                  time=time.time() - async_start_time))
    for item in ASYNC_CONTENT_QUEUE:
        print(item)
    sync_start_time = time.time()
    sync_qiubai(base_url)
    print('同步爬虫抓取 {number} 条段子， 用时 {time}'.format(number=len(SYNC_CONTENT_QUEUE),
                                                  time=time.time() - sync_start_time))


if __name__ == '__main__':
    main()
# https://github.com/Agnewee/MySpider