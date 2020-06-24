# 在属性名和方法名前面加上‘__’那么定义的属性和方法就是私有属性和方法
class Person(object):
    def __init__(self, name, age):
        # 共有属性
        self.name = name
        # 私有属性，只能在本类中使用，不能再类外部使用
        # 注意：私有属性只能在本类中修改，不能再外界修改
        self.__age = age

    def show(self):
        # 在内部可以使用私有方法和属性
        print(self.name, self.__age)
        print(self.name)

    def __money(self):
        print("100万")


person = Person("李四", 20)
print(person.name)
person.show()
# 私有属性和方法在外界访问不了
# print(person._age)


# # person.__money()
#
# print(person.__dict__)
# # 本意是修改私有属性
# # 这里不是修改了私有属性，而是給对象添加了一个__age的对象属性
# person.__age = 22
# print(person.__age)
# print(person.__dict__)
# # 查看私有方法
# # print(Person.__dict__)


# 在python里面私有属性和方法没有做到绝对私有，只是把私有属性和方法进行了一个名字的伪装
print(person.__dict__)
person._Person__age = 34
print(person._Person__age)
print(person.__dict__)

person._Person__money()


### 子类继承父类不能直接使用父类的私有属性和私有方法

class Person(object):
    def __init__(self, age):
        self.__age = age

    def __show(self):
        print("我是一个私有方法")


class Student(Person):
    def show(self):
        # 访问父类里面的私有方法和属性
        print(self.__age)
        self.__show()


student = Student()
student.show()


# student = Student()
# print(student.__age)
# student.__show()

