class Person(object):
    # 定义对象方法：在方法的参数里面有self表示对象方法
    def show(self):
        print('我是人类')
    # 定义类方法：cls表示当前类（调用类方法不需要实例化，可以在类方法中调用对象方法）
    @classmethod
    def show_info(cls):
        print(cls)
        print("我是一个类方法")

    # 定义静态方法：静态方法和当前类没有关系，不会使用self和cls
    @staticmethod
    def show_msg():
        print('我是一个静态方法')

    # 应用场景：类方法可以修改类属性
    @classmethod
    def set_type(cls, type):
        cls.__type = type

    @classmethod
    def get_type(cls):
        return cls.__type

    # ---------------------- 对象方法是最通用的方法去，可以修改对象属性和类属性
    def instance_set_type(self, type, name):
        # 获取对象所对应的类
        self.__class__.__type = type
        self.name = name

    def instance_get_type(self):
        print(self.name)
        return self.__class__.__type

    @staticmethod  # 提示：既不需要当前对象和当前类
    def sum_num(num1, num2):
        return num1 + num2


# 创建对象
p = Person()
p.show()
p.show_info()
p.show_msg()

p.set_type('白种人')
result = p.get_type()
print(result)

p.instance_set_type('黑人种', "小饼")
print(p.instance_get_type())

result = p.sum_num(1, 2)
print(result)


# 类调用静态方法和类方法不需要传入当前类，如果类调用对象方法需要传入一个实例
Person.show_msg()
# Person.show(p)
Person.show_info()

# self便是一个具体的实例本身，如果用了staticmethod，那么就可以无视这个self，
# 将这个方法当成一个普通的函数使用；cls表示这个类本身。

print("------------------------------------------")
# ----------------------例子----------------------------


class A(object):
    # 属性默认为类属性（可以直接被类本身调用）
    num = "类属性"

    # 实例化方法（必须实例化之后才能被调用）
    def func1(self):
        # self:表示实例化类后的地址id
        print("func1")
        print(self)

    # 类方法（不需要实例化类就可以被类本身调用）
    @classmethod
    def func2(cls):
        # cls表示没有被实例化的类本身
        print("func2")
        print(cls)
        print(cls.num)
        cls().func1()

    # 不设置参数默认self参数的方法（该方法也是可以直接被类调用的，但是这样做不标准）
    def func3():
        print("func3")
        print(A.num)  # 属性是可以直接类本身调用的


# A.func1() 这样调用时会报错：因为func1（)调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的
A.func2()
A.func3()
