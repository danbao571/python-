# 迭代器：在类里面有__iter__和__next__的方法创建的对象就是迭代器，作用：根据数据的位置获取下一位置的数据
class MyIterator(object):
    def __init__(self):
        self.my_list = [4, 5, 6, 7]
        self.current_index = 0

    def __iter__(self):
        # 返回一个迭代器对象
        return self

    def __next__(self):
        if self.current_index < len(self.my_list):
            # 获取迭代器中下一个值
            result = self.my_list[self.current_index]
            self.current_index += 1
            return result
        else:
            # 抛出停止迭代的异常
            raise StopIteration


# 创建迭代器
my_iterator = MyIterator()
# 使用next函数获取迭代器中下一个值
# result = next(my_iterator)
# print(result)
#
# result = next(my_iterator)
# print(result)

# for循环内部会自动停止迭代异常
for vaule in my_iterator:
    print(vaule)

