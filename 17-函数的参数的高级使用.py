def show(name, age, *args, **kwargs):
    print(name, age, args, kwargs)

# 不能使用下面的方式进行调用，因为前面使用了关键字后面不能使用位置参数
# show(name = '神仔', 29, 89, 0, c = 1, b = 'as')
# 注意：**kwargs必须放到所有参数最后面

# show('神仔', 29, 89, 0, c = 1, b = 'as')


def show(name,  *args, age=17, **kwargs):
    print(name, age, args, kwargs)

show('神仔', 29, 89, 0, c = 1, b = 'as')

# 如果有必选参数和缺省参数，那么缺省参数要放到必选参数后面