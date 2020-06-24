# 指明创建对象的时候不能再添加其他属性，只能是指定的属性
class Student(object):
    __slots__ = ('name', 'age')

    def __init__(self, name, age):

        self.name = name
        self.age = age


stu = Student('sad', 20)
# stu.sex = '男'
print(stu.name, stu.age)
stu.name = '王五'
print(stu.name, stu.age)
