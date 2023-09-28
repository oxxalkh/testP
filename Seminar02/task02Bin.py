# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

a = 23
result = ""
result_bin = bin(a)
while a > 0:
    result = str(a % 2) + result
    a //= 2
if result == result_bin[2:]:
    print(f'{result}=={result_bin} ')
else:
    print('ERROR')

a = 888
result = ""
result_oct = oct(a)
while a > 0:
    result = str(a % 8) + result
    a //= 8
if result == result_oct[2:]:
    print(f'{result}=={result_oct} ')
else:
    print('ERROR')

