# html与xml的区别：xml为json前身，是前端移动和后台交互的数据格式，以字典形式存放数据
# 以<key>value</key>的形式保存数据；html用于展示数据。以固定标签组成。
from lxml import etree
# 模糊查询
# div_list = html.xpath("//div[contain(@class,"a")]"),表示查询所有包含class属性为“a”的div
# div_list = html.xpath("//head/following-sibling::*[1]"),表示取head的同级标签body
# xpath取下标由一开始
data = '''
     html代码。。。。
'''
html = etree.HTML(data)
