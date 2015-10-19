#-*-coding=utf-8-*-
import urllib.request
import io
import gzip

i=180


'''
函数接受一个URL链接然后返回一个未经过任何处理的网页
'''
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36')
    req.add_header('Accept-encoding', 'gzip')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html
'''
函数接受一个URL链接然后返回一个经过解码处理之后的网页
'''
def get_page(url):
    bs=url_open(url)
    bi = io.BytesIO(bs)
    gf = gzip.GzipFile(fileobj=bi, mode="rb")
    '''page=gf.read()
    charS=page.info().getparam('charset')
    return page.decode(charS,'ignore').encode('utf-8')
    '''
    return gf.read().decode('gbk','ignore')
'''
函数接受一个网页参数然后将网页保存到文件中，文件名以此为1.html 2.html ..... 
'''
def save_file(html):
    global i
    file=open(str(i)+'.html',"w")
    i+=1
    file.write(html)
    file.close()

#html=get_page('http://www.baidu.com')


file=open('url.txt')
url=file.readline()
while(''!=url):
    html=get_page(url)
    name=url.split('.')[1]
    save_file(html)
    url=file.readline()
    print(name)
    print(url)




