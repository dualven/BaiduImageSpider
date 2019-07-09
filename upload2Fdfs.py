#!/usr/bin/env python
# Filename: upload2Fdfs
import urllib.request
import urllib.parse
import requests
def uploadlocal(picpath):
    url = 'http://10.60.2.175:28091/file/uploadlocal'
    data ={ 'filepath':picpath} 
    headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
    postdata = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request( url=url,data=postdata,headers=headers)
    response = urllib.request.urlopen(req)
    page_source = response.read()
    print(page_source)
def uploadlocal2(picpath):
    files = {'file':open(picpath, 'rb')}
    headers = {"content-type": "multipart/form-data"}
    url = 'http://10.60.2.175:28091/file/upload'
    data ={ 'thumbImage':'true'} 
    req = requests.post( url,files=files,data=data)
    print(req.text)
if __name__ == '__main__':
#   uploadlocal('/home/fdfs_data/111/9.jpeg')
   uploadlocal2('/home/python/BaiduImageSpider/111/9.jpeg')
