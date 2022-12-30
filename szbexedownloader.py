import requests
import re
import webbrowser
url=r'https://adl.netease.com/d/g/sv/c/gwpc?type=android'
html=requests.get(url)
page_got=re.findall(r'android_link = android_type \? "(.*?)" :',html.text)
apk_url=page_got[0]
exe_url=apk_url.replace('apk','exe')
webbrowser.open(exe_url)

