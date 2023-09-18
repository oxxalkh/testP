import math
import decimal
import fractions

print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')

pi = decimal.Decimal(
    "3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375")
print(pi)
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)

decimal.getcontext().prec = 120
science = 2 * pi * decimal.Decimal(23.452346) ** 2
print(science)

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)

#справка
print(dir(math))
print(help(math.degrees))


# ● abs(x) — возвращает абсолютное значение числа x, число по модулю.
# ● divmod(a, b) — функция принимает два числа в качестве аргументов и
# возвращает пару чисел — частное и остаток от целочисленного деления.
# Аналогично вычислению a // b и a % b. ответ выводится в кортеже
# ● pow(base, exp[, mod]) — при передаче 2-х аргументов возводит base в
# степень exp. При передаче 3-х аргументов, результат возведения в степень
# делится по модулю на значение mod.
# ● round(number[, ndigits]) — округляет число number до ndigits цифр
# после запятой. Если второй аргумент не передать, округляет до ближайшего
# целого.

x = -76
print(abs(x))

a = 270
b = 53
print(divmod(a, b))

print(pow(a, b, 3))

print(round(3.66666666778990, 3))



