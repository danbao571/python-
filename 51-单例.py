# 单例：在应用程序中不管创建多少次对象只有一个实例对象


class Person(object):

    # 私有的属性
    __instance = None

    # 创建对象
    def __new__(cls, *args, **kwargs):
        # if cls.__instance == None:
        if not cls.__instance:
            print('创建对象')
            # 把创建的对象给类属性
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        print('初始化')


p1 = Person()
p2 = Person()
print(p1, p2)
