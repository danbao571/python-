# 指定__all__表示from 模块名 import *只能使用指定的功能代码。
__all__ = ['show', 'Student']

# 定义全局变量

g_num = 10


# 定义函数
def show():
    print('我是一个函数')


# 定义类
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_msg(self):
        print(self.name, self.age)
