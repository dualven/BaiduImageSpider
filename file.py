#!/usr/bin/evn python
#Filename: file

import requests

url='http://10.60.2.175:28091/file/upload'
files={'file': open('/home/python/BaiduImageSpider/111/9.jpeg','rb')}
r= requests.post(url,files=files)
print(r.text)

