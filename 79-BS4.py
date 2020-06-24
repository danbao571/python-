from bs4 import BeautifulSoup

html = '''
<html>
    <head>
        <title id="title">楞眼鹅</title>
    </head>
    <body>
        <p class="url"><a href="http://www.baidu.com">百度</a>哈哈</p>
        <p class="url" id="django"><a href="http://www.jingdong.com">京东</a>嘻嘻</p>
        <p class="url"><a href="http://www.taobao.com">淘宝</a>呵呵</p>
        <p class="url"><a href="http://www.tianmao.com">天猫</a>嘿嘿</p>
    </body>
</html>

'''
soup = BeautifulSoup(html, "lxml")  # .prettify()格式化，使结构整洁。
print(soup)
# 取标签属性值，以字典形式保存
href = soup.select('a')[3].attrs
print(href)
# 取标签属性值，以列表形式保存
attrs = soup.select('p')[0].get('class')
print(attrs)
# 取标签文字内容
content = soup.select('a')[3].string
print(content)

# get_text()方法获取该标签下所有文字内容(包括子标签) 下面四条结果均为京东嘻嘻
result = soup.select('.url')[1].get_text()
result = soup.select('p[id="django"]')[0].get_text()
result = soup.select('#django')[0].get_text()
result = soup.select('body p')[1].get_text()
print(result)

# string和get_text()都可以取内容，但string只能在只有一层内容情况下取，get_text()可以取多级标签的内容。
# 如上面p标签又有京东，其下a标签又有嘻嘻，用string会取不出，return的是None。
#  xpath下标从1开始
