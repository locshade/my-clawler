#������Ҫ��¼�ڿ����Ĺ����������������Լ��������Ĺ��̺ͽ��������

##��ҳ����ͷ��
�ڱ�дpython�����ʱ���һ��������������Ǳ���վ��forbidden���������Ľ����������ʹ��chrome���е��Ե�ʱ��۲���ҳ����ͷ��أ�Ȼ����������õ�������ʹ��python����ҳ��ʱ������user-geent�������������Ĵ������£�

```python
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html
```
�����е�Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36��ͬ�ĵ����ϲ�һ����ͬ��


##����
����Ҫ�������ҳ��Ҫ��������ҳ�����Ա�������Ƚ���Ҫ��������ϸ�ļ�¼һ�±�����ص���Ϣ��

1�������һ��Ҫ����
```python
#coding:utf-8
```
2�����ԵĹ�����һֱ�����ı������⣬������һ�����ӣ�

[python�����ַ������](http://my.oschina.net/leejun2005/blog/74430)