def fun_ext():
    
    x = float(input("введите х: "))
    y = int(input("введите отрицательное целое число: "))
    if y > 0:
        print("надо отрицательное...")
        
    else:
        return(x ** y)

a = fun_ext()
print(a)
