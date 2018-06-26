# -*- coding:utf-8 -*-
import urllib.error
import urllib.request
import urllib
from bs4 import BeautifulSoup
import re

savepath = ""
cookies = "_T_WM=fc59da180d669b6fc69394664b834145; SCF=AlHnKfoTijLAi7EYPlzfv_rIGs-ZCb7OqaVicRuEfIYAhC8SYrJBXMh0tVFt3UBMkqAkOj3BXYmAcEqAs4x9RX8.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5iRESZYIVKcegp-.ni6KSO5JpX5KMhUgL.Fo-EehzfeKqR1hq2dJLoI7yPgH241KLoq7tt; H5_INDEX_TITLE=WYQ999cc; H5_INDEX=0_all; SUB=_2A252NPUpDeRhGeNM61AU8SjEwzqIHXVV1pthrDV6PUJbkdAKLUuhkW1NTljRJ51gZT1chMKPaN4GPtL3CPHcKjNf; SUHB=0d4-6O993bFdJx; SSOLoginState=1529906553"
uid = "2084348103"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
urlinit = 'https://weibo.cn/u/'

def main():

    weibologinheader = {'User-Agent': UA,'Cookie': cookies}

    imglist_reg = r'href="(https://weibo.cn/mblog/picAll/.{9})"'

    imglist_pattern = re.compile(imglist_reg)

    img_reg = r'src="(http://w.{2}\.sinaimg.cn/(.{6,8})/.{32,33}.(jpg|gif))"'

    img_pattern = re.compile(img_reg)
    
    page = 4
    
    #while True:
    url = "https://weibo.cn/u/"+uid+"?filter=%1&page="+str(page)
    blogpage = openhtml(url,weibologinheader)
        
    soup = BeautifulSoup(blogpage,"html.parser")
    print(soup.prettify())
    blogs = soup.find_all(id=re.compile(r'^M_'))
    for blog in blogs:
        print(blog)
        print("\n\n")
        



def openhtml(url,header):
    
    req = urllib.request.Request(url,headers=header)
    print("visiting:"+urlinit+uid)
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html

main()
