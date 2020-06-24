# 单继承：子类只继承一个父类
# 子类继承父类可以使用父类的方法和属性
# 继承的好处：是子类可以复用父类的代码


class Person(object):
    def __init__(self):
        self.name = '张三'
        self.age = 18

    # 对象方法:当方法参数有self表示是对象方法
    def show(self):
        print(self.name, self.age)


# 学生类是子类，小括号里面是父类
# 父类（基类），子类（派生类）
class Student(Person):
    pass


xiao_lan = Student()
xiao_lan.show()
print(xiao_lan.name, xiao_lan.age)