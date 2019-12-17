#coding:utf-8
import requests
import urllib3
import random
import time, re
import base64
import urllib, json
import urllib.request
from urllib import parse
from mytoken import GetToken
import operator
 
faceDetectUrl = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
# 根据人脸检测的颜值打分，判断是否下载
def IfDownLoad(pic, token):
    img = base64.b64encode(pic)
    print(token);
    params = {"image_type":"BASE64","face_field":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities","image":img }
    params = parse.urlencode(params).encode("utf-8");
    request_url = faceDetectUrl + "?access_token=" + token
    print(request_url)
    temprequest = urllib.request.Request(url=request_url, data=params)
    temprequest.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(temprequest)
    print(response);
    content = response.read()
    print(content);
    if content:
        js = json.loads(content)
        print(js);
        for item in js['result']['face_list']:
            print ("age: %d, beauty: %d" % (item['age'], item['beauty']));
            if 0 == operator.eq('female', item['gender']):
                if (item['age']<29)and(item['beauty']>55):      # 只下载女孩，年龄小于 29，颜值大于 55分
                    return True
    return False
 
def DownLoad(url, i):
    fp = open("pic/%d.jpg"%i, "wb+")
    fp.write(url)
    fp.close()
 
 
 
if __name__ == "__main__":
    # 获取网页源代码
    word="张天爱";
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn=';
    data = requests.get(url)
#    print (data.content)
 
    # 获取链接并判断是否下载
    pattern = re.compile(r'.*?"objURL":"(.*?)",', re.S)
    result = pattern.findall(data.content.decode('utf-8'));
    i = 0
    token = GetToken()['access_token'];
    for item in result:
        print (item)
        try:
            pic = requests.get(item, timeout=10)
            if(True == IfDownLoad(pic.content, token)):
                DownLoad(pic.content, i)
                i = i + 1
                print(i);
        except Exception as e:
           print(e);
#        break;
    print("the end");
 
