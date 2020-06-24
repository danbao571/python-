# 循环（for while）：根据条件循环执行某种操作
# 提示：while会循环判断条件是否成立，如果条件成立会执行while循环语句，
# if判断只会判断一次

# 1-5循环5次
num = 2
while num <= 5:
    print(num)
    num += 1

print("---------------")

# for循环一般会结合range使用，range是一个范围
# 1-5循环5次
# range(起始位置，结束位置，步长)
# range（1,5），1：开始数据， 5：结束数据，range里面结束数取不到
for value in range(1, 6, 1):
    print(value)

# for 和 while 可以结合else语句使用
print("-------------------")
num = 5
while num >= 1:
    print(num)
    num -= 1
else:
    print("循环语句执行结束")

print("-------------------")

for value in range(1, 9, 2):
    print(value)
else:
    print("循环执行结束")
