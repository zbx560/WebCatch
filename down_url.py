from urllib import request, parse
import os
import time
import requests,time,threading
from hashlib import md5
from lxml import etree
import urllib
import requests, re

def down_mp4(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    url = 'http://zuida.downzuida.com/1909/X三国-01.mp4'
    downsize = 0
    startTime = time.time()
    for i in range(10,95):
        down_url=url[0:-6]+'0'+str(i)+url[-4:]
        movie_name=down_url[-9:]
        req = requests.get(down_url,headers=headers,stream=True,verify=False)
        with(open('D:/三国/'+movie_name,'wb')) as f:
            for chunk in req.iter_content(chunk_size=1000000):
                if chunk:
                    f.write(chunk)
                    downsize+=len(chunk)
                    line='file %s downloading %.2f MB/s - %.2f MB, 共 %.2f  MB'
                    line=line % (
                        movie_name,downsize/1024/1024/(time.time() - startTime),downsize/1024/1024,downsize/1024/1024
                    )
                    print (line)
    # dir = "/d/三国"
    # print(down_url[-9:-4])
    # urllib.request.urlretrieve(down_url, dir ,down_url[-9:])
# <a href="/ju/17338/play-132038" target="_blank">第01集</a>
# print(soup.prettify())
# print(res.findAll('a',href=True))
# for a in soup.findAll('link',type='text/css'):
#   print(a)
#   if re.findall('target', a['href']):
#
#     print("Found the URL:", a['href'])
