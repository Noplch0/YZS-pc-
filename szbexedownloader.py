import requests
import re
import webbrowser
import os
url=r'https://adl.netease.com/d/g/sv/c/gwpc?type=android'
print('这是一个SZB下载器')
print('作者:Noplch')
print('源码地址:https://github.com/Noplch0/YZS-pc-.git')
print('按任意键以开始下载(进入牢房)...')
os.system('pause>nul')
html=requests.get(url)
page_got=re.findall(r'android_link = android_type \? "(.*?)" :',html.text)
apk_url=page_got[0]
exe_url=apk_url.replace('apk','exe')
webbrowser.open(exe_url)

