# 序列化：把内存中的数据保存到本地，可以做到持久化存储
import pickle  # 比较通用，可以序列化任意对象类型
# my_list = [{'name':'李四', 'age':20},{'name':'王五', 'age':23}]
# file = open('my_list.serialize', 'wb')
# # 得到的数据是二进制数据，想要写入到文件，文件的访问模式是‘wb’
# pickle.dump(my_list, file)
#
# file.close()

# 反序列化：把文件中的数据读取出来，获得到一个python对象
# file = open('my_list.serialize','rb')
# my_list = pickle.load(file)
#
# print(my_list)
# file.close()


class Student(object):
    def __init__(self):
        self.name = '张三'
        self.age = 20

# stu = Student()
# file = open('stu.serialize', 'wb')
# # 序列化自定义类型对象
# pickle.dump(stu, file)
# file.close()


file = open('stu.serialize', 'rb')
# 反序列化
stu = pickle.load(file)
print(stu.name, stu.age)

file.close()
