#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re
import requests
import time
from selenium import webdriver

word = raw_input("Input key word: ")
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"
}
requests.get(url, headers=headers)

# url = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1460997499750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%B0%8F%E9%BB%84%E4%BA%BA'

html = requests.get(url).text
option = webdriver.ChromeOptions()
option.add_argument('headless')  # 设置option
driver = webdriver.Chrome(options=option)
# driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
i = 550
a = 0
n = 0
while True:
    for each in pic_url:
        print(each)
        name = each[-9:]
        try:
            pic = requests.get(each, timeout=10)
        except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
            a += 1
            print ('【错误】当前图片无法下载')

            continue
        string = 'C:/Users/xlh/Desktop/mm\\' + str(i) + '.jpg'
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
        print(i)
        if i % (21-a) == 0:
            a = 0
            break
    driver.find_element_by_link_text('下一页').click()
    time.sleep(1)
    print('test pass: element found by link text')

    handle = driver.current_url
    print(handle)
    html = requests.get(handle).text
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)








