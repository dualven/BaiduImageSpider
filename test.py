#!/usr/bin/env python
import re
import upload2Fdfs as up
str = " duan xiongwen is good! 15900402562"
matchobj = re.search(r'\D+',str, re.M|re.I)
#上面的非数字,下面的是数字
matchobj2 = re.search(r'\d+',str, re.M|re.I)
print(matchobj.group())
print(matchobj2.group())

up.uploadlocal('/home/fdfs_data/111/10.jpg')
