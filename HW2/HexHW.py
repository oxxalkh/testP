# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def decimal_to_hexadecimal(numb):
    hex_digits = "0123456789ABCDEF"  # Строка с шестнадцатеричными цифрами
    hex_string = ""
    while numb > 0:
        remainder = numb % 16  # Получаем остаток от деления на 16
        hex_digit = hex_digits[remainder]  # Получаем шестнадцатричную цифру
        hex_string = hex_digit + hex_string  # Добавляем цифру в начало
        # шестнадцатеричного числа
        numb //= 16  # Выполняем целочисленное деление на 16
    return hex_string


def decimal_to_hexadecimal_check(numb):
    hex_string = hex(numb)  # Используем встроенную функцию hex()
    # для преобразования в шестнадцатеричное представление
    return hex_string


num = int(input("Введите число: "))
hex_str = decimal_to_hexadecimal(num)
hex_check = decimal_to_hexadecimal_check(num)

print(f"Шестнадцатеричное представление числа {num} - 0x{hex_str}")
print(f"Шестнадцатеричное представление числа {num} - {hex_check}")
