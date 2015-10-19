#coding:utf-8
import urllib.request
import io
import gzip
import re

'''
这个程序是使用python3语法格式进行编写的，程序的功能是首先根据初始URL获得网页
然后将其中的链接过滤出来后存放到url.txt这个文件中然后这个文件。

与此程序配套的程序是getUrlByPage.py这个文件，这个文件是将url.txt这个文件中的所有
超链接下载并保存。

'''


'''
函数接受一个URL链接然后返回一个网页（没有经过解码等处理）
'''
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36')
    req.add_header('Accept-encoding', 'gzip')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

	
'''
函数接受一个URL链接然后将解码后的网页返回。
'''
def get_page(url):
    bs=url_open(url)
    bi = io.BytesIO(bs)
    gf = gzip.GzipFile(fileobj=bi, mode="rb")
    '''page=gf.read()
    charS=page.info().getparam('charset')
    return page.decode(charS,'ignore').encode('utf-8')
    '''
    return gf.read().decode('utf-8')



page=get_page('http://www.huanqiu.com/')
p=r'href="(http:[^<>]+?\.html)"'
result=re.findall(p,page)


file=open('url.txt','w')
for each in result:
    file.write(each+"\n")
