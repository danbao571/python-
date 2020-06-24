list = [2, 45, 5, 1, 546, 0]
# sorted()

def Bubbling(list):
    for j in range(0, len(list) - 1):
        for i in range(0, len(list) - 1 - j):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    print(list)


Bubbling(list)
h = sorted(list)
print(h)
