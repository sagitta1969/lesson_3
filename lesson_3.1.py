def division(x, y):
''' задание 1'''
    if y == 0:
        print("деление на ноль")
    else:
        return x / y

a = int(input("введите х: "))
b = int(input("введите у больше нуля: "))
print(division(a, b))
