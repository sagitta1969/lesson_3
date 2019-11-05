def users(name, l_name, b_day, u_sity, u_email, u_tel):
    return(name.title() + ', ' + l_name.title() + ', ' + b_day + ', ' + u_sity.title() + ', ' + u_email + ', ' + u_tel)

name = (input("введите имя: "))
l_name = (input("введите фамилию: "))
b_day = (input("введите день раждения: "))
u_sity = (input("введите город: "))
u_email = (input("введите эл почту: "))
u_tel = (input("введите телефон: "))

print(users(name, l_name, b_day, u_sity, u_email, u_tel))