import urllib.request
def get_page():
   url = 'http://www.baidu.com/'
   res = urllib.request.urlopen(url=url)
   page_source = res.read().decode('utf-8')
   print(page_source)


if __name__ == '__main__':
    get_page()
