#这里主要记录在开发的过程中碰到的问题以及解决问题的过程和解决方案等

##网页请求头部
在编写python爬虫的时候第一个碰到的问题就是被网站给forbidden，这个问题的解决方案是在使用chrome进行调试的时候观察网页请求和返回，然后根据搜索得到可以在使用python打开网页的时候设置user-geent这个参数，具体的代码如下：

```python
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html
```
代码中的Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36不同的电脑上不一定相同。


##编码
由于要处理的网页主要是中文网页，所以编码问题比较重要，这里仔细的记录一下编码相关的信息。

1：代码第一行要加上
```python
#coding:utf-8
```
2：调试的过程中一直碰到的编码问题，这里是一个链接：

[python处理字符串相关](http://my.oschina.net/leejun2005/blog/74430)