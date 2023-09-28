# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях
n = 'RTyhjk'
if n.isdigit():
    # if '-' in n:
    #     n = n.replace('-', '')
    #     flag = True
    #     if flag:
    #         print(- int(n))
    #     else:
    #         print(int(n))
    print(int(n))
if '.' in n:
    if '-' in n:
        n = n.replace('-', '')
        flag = True
    left, right = n.split('.')
    if left.isdigit() and right.isdigit():
        if flag:
            print(- float(n))
        else:
            print(float(n))
if n != n.lower():
    print(n.lower())
else:
    print(n.upper())

