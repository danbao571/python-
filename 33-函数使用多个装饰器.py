def decorator1(func):
    print("1")
    def inner():
        print('-'*10)
        func()
    return inner

def decorator2(func):
    print("2")
    def inner():
        print('+'*10)
        func()
    return inner

@decorator1
@decorator2
def show():
    print('asda')

show()
# 装饰器在被装饰函数定义好一周就会执行（即（2,1）不需要被装饰函数调用也会输出）