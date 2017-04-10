# -*- coding: utf-8 -*-

import os, urllib.request, re

class Spider(object):
    def __init__(self):
        self.urlSite = 'http://mm.taobao.com/json/request_top_list.htm'

    def getPage(self, index):
        url = self.urlSite + "?page=" + str(index)
        content = urllib.request.urlopen(url).read()
        return content.decode('gbk');

    def getContents(self, index):
        page = self.getPage(index);
        pattern = re.compile(r'<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            contents.append([item[0], item[1], item[2], item[3], item[4]])
        return contents

    def makeDir(self, path):
        path = path.strip()
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            return True
        else:
            return False

    def saveIcon(self, url, name):
        fileName = name+'/'+name+'.jpg'
        result = urllib.request.urlopen('https:'+url).read()
        f = open(fileName, 'wb')
        f.write(result)
        f.close()

    def saveBreif(self, name, age, address):
        fileName = name+'/'+name+'.txt'
        data = name+'\n'+age+'\n'+address+'\n'
        f = open(fileName, 'w')
        f.write(data)
        f.close()

    def savePage(self, index):
        items = self.getContents(index)
        print(items)
        for item in items:
            print(item[0], item[1], item[2], item[3], item[4])
            self.makeDir(item[2])
            self.saveIcon(item[1], item[2])
            self.saveBreif(item[2], item[3], item[4])



spider = Spider()
spider.savePage(1)

