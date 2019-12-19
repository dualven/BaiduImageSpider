import requests
 
# url 即为图片网页的网址
url = "https://image.baidu.com/search/index?tn=baiduimage&【...】"
 
data = requests.get(url)
print (data.content)
 
# 正则表达式的使用，可参照上一节
#pattern = re.compile(r'.*?"objURL":"(.*?)",', re.S)
#result = pattern.findall(data.content)
#for item in result:
#    print (item)
