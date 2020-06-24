# __new__:当创建对象的时候会调用__new__(实例化对象， 开辟空间内存）
# __init__:当对象创建案例完成会调用init方法给对象添加属性及初始化（对实例对象进行初始化操作）
# new方法和init方法会在创建对象地自动被调用，new会再init之前被调用。
# new方法实例化对象(创建一个内存空间），将实例化的对象return给init，init再对这个实例对象
# （内存空间）进行初始化属性，如果new方法没有return，init方法不会被调用。
# new方法的参数是cls-当前类本身，init方法的参数是self-实例化的对象。


# 创建对象会自动调用两个方法，先调用__new__,后调用__init__
class Student(object):
    # 不重写new方法时默认调用父类的new方法
    def __new__(cls, name, age):
        print("创建对象")
        print(name, age)
        return object.__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('初始化')


stu = Student('李四', 20)
