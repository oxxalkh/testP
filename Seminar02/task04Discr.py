# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

a, b, c = -5, 6, -7
d = b ** 2 - 4 * a * c
x1 = (-b + d ** 0.5) / 2 * a
x2 = (-b - d ** 0.5) / 2 * a
print(f'{x1}: {type(x1)} \n {x2}: {type(x2)}')
