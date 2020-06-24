# 生成器是一个特殊的迭代器，也就是说它可以通过next函数和for循环取值
# 迭代器和生成器的好处就是：根据需要每次生成一个值，不像列表把所有的数据都准备好，这样列表比较占用内存

# 1.使用生成器的表达式
# result = [x for x in range(4)]（列表表达式）
# print(result)

result = (x for x in range(4))
print(result)

# 测试：使用next获取下一个值
# value = next(result)
# print(value)

for value in result:
    print(value)


# 2.使用yield创建生成器
def show_num():
    for i in range(5):
        # 代码遇到yield会暂停，然后把结果返回出去，下次启动生成器时在暂停位置继续执行下去
        # yield特点：可以返回多次值，return只能返回一次值
        print('123')
        yield i  # 当前次yield后面代码不会执行
        print('789')


g = show_num()
value = next(g)
print(value)
value = next(g)
print(value)
# 获取多次值
for value in g:
    print(value)
