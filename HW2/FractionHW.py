# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction
import math


def string_fractions(frac1_str, frac2_str):
    # Преобразуем дроби из строк в числа
    num1, den1 = map(int, frac1_str.split("/"))
    num2, den2 = map(int, frac2_str.split("/"))

    return num1, den1, num2, den2


def process_fractions(num1, den1, num2, den2):
    # Вычисляем сумму дробей
    sum_fr_num = num1 * den2 + num2 * den1
    sum_fr_den = den1 * den2
    summ_frac = common_denominator(sum_fr_num, sum_fr_den)

    # Вычисляем произведение дробей
    pr_fr_num = num1 * num2
    pr_fr_den = den1 * den2
    pr_frac = common_denominator(pr_fr_num, pr_fr_den)

    return summ_frac, pr_frac


def common_denominator(a, b):
    # сокращаем дробь
    gcd = math.gcd(a, b)
    if gcd > 1:
        a /= gcd
        b /= gcd

    return a, b


def process_fractions_check(num1, den1, num2, den2):
    # Создание объектов Fraction для каждой дроби
    fraction_obj1 = Fraction(num1, den1)
    fraction_obj2 = Fraction(num2, den2)
    # Вычисление суммы и произведения дробей
    sum_fraction = fraction_obj1 + fraction_obj2
    product_fraction = fraction_obj1 * fraction_obj2
    return sum_fraction, product_fraction


frac1_string = input("Введите первую дробь в формате a/b: ")
frac2_string = input("Введите вторую дробь в формате a/b: ")

numerator1, denominator1, numerator2, denominator2 = string_fractions(
    frac1_string, frac2_string)

sum_frac1, prod_frac1 = process_fractions(numerator1, denominator1,
                                          numerator2, denominator2)

print(f"Сумма дробей: {frac1_string} и {frac2_string} - "
      f"{int(sum_frac1[0])}/{int(sum_frac1[1])}")
print(
    f"Произведение дробей: {frac1_string} и {frac2_string} -"
    f" {int(prod_frac1[0])}/{int(prod_frac1[1])}")

sum_frac2, product_frac2 = process_fractions_check(numerator1, denominator1,
                                                   numerator2, denominator2)

print(f"Сумма дробей:  {frac1_string} и {frac2_string} - {sum_frac2}")
print(f"Произведение дробей: {frac1_string} и {frac2_string} - {product_frac2}")
