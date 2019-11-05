def my_func(nam_1, nam_2, nam_3):
    a = [nam_1, nam_2, nam_3]
    a.remove(min(a))
    return(sum(a))

nam_1 = int(input("введите число 1: "))
nam_2 = int(input("введите число 2: "))
nam_3 = int(input("введите число 3: "))

print(my_func(nam_1, nam_2, nam_3))