# 魔法方法：当需要完成某个功能操作时，会自动调用某个方法，比如：__init__，当对象初始化的时候调用
# 魔法方法表现形式：以__开始，以__结束。

# init


class Student(object):
    def __init__(self, name, age):
        # self：表示当前对象
        # 给对象初始化，添加对象属性
        print("对象初始化了")
        self.name = name
        self.age = age

    # 显示学生信息的方法
    def show_info(self):
        print(self.name, self.age)


student = Student("德芙", 20)
student.show_info()
student1 = Student("王五", 50)
student1.show_info()

# -----------------__str__-----------------

# __str__:当使用print打印对象的时候回自动调用对象的__str__方法


class Person(object):
    # 给对象添加属性及对属性进行初始化
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 返回对象的描述信息
    def __str__(self):
        return "我叫：%s 年龄：%d" % (self.name, self.age)


# 创建对象
# 调用init方法使用位置参数传参
# person = Person("张三",20)
person = Person(name="李四", age=20)
# print(person.name, person.age)
print(person)


# ------------------__del__-----------------------

# __del__：当对象释放的时候回自动调用__del__方法

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 当对象的引用计数为0时会调用del魔法方法
    def __del__(self):
        print("对象释放了：", self)


# 创建对象
xiao_ming = Person("小明", 20)
print(xiao_ming)
