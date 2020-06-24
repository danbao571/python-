import json  # 只能支持部分数据类型，不通用，比如：列表，字典，int类型；自定义类型不可以需要额外指定
# my_list = [{'name':'李四', 'age':20}, {'name':'王五', 'age':23}]
#
# file = open('my_list.txt', 'w', encoding='utf-8')
# json.dump(my_list, file)
# file.close()

file = open('my_list.txt', 'r', encoding='utf-8')

# 反序列化
my_list = json.load(file)

print(my_list)
file.close()


class Student(object):
    def __init__(self):
        self.name = '李四'
        self.age = 20


file = open('stu.txt', 'w', encoding='utf-8')
stu = Student()
# 序列化对象本质是把对象的属性进行保存
json.dump(stu.__dict__, file)

file.close()

# 对字符串和dict list转换loads dumps
# str->list
data = '[{"name": "神仔", "age": "20"},{"name": "lyj", "age": "22"}]'
list_data = json.loads(data)
print(data, list_data)
print(type(data), type(list_data))
# list->str
list_1 = [{"name": "神仔", "age": "20"}, {"name": "lyj", "age": "22"}]
str_1 = json.dumps(list_1)
print(type(str_1))
# 对文件对象和dict list转换load dump
# 写入文件
list_2 = [{"name": "神仔", "age": "20"}, {"name": "lyj", "age": "22"}]
json.dump(list_2, open('02data.json', 'w'))

# 读取文件json ---- list dict
fp = open('02data.json', 'r')
result = json.load(fp)
print(result)
print(type(result))

