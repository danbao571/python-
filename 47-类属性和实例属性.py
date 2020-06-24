# 类属性是在方法外和在类内部定义的属性
# 实例属性是在init方法里面定义的属性


class Person(object):
    # 类属性，对象没有创建就想使用这个属性可以定义成类属性
    type = "黄种人"

    def __init__(self):
        # 实例（对象）属性
        self.name = "小明"
        self.age = 20


# 使用类访问类属性
print(Person.type)
# 使用类不能访问实例属性
# print(Person.age)

# 修改类属性
Person.type = '白种人'
print(Person.type)
# 查看类属性和方法
print(Person.__dict__)


# --------------实例属性---------------------
# 创建对象
xiao_ming = Person()
# 使用实例访问对象属性
print(xiao_ming.name)
# 对象可以访问类属性
print(xiao_ming.type)
# 对象不能修改类属性，其实是添加了一个对象
print('-----------------------')
# print(Person.__dict__)
# print(xiao_ming.__dict__)
# xiao_ming.type = '黑种人'
# print(xiao_ming.type)
# print(Person.__dict__)
# print(xiao_ming.__dict__)

print(xiao_ming.__dict__)
# 使用实例修改对象属性
xiao_ming.name = "李四"
print(xiao_ming.name)
print(xiao_ming.__dict__)


# 总结：类属性的操作由类完成，对象属性的操作由对象完成
# 对象可以访问类属性
