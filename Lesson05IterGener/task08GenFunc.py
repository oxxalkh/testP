# Внутри функции создали переменную для хранения очередного числа и
# результирующий список. Далее в цикле перебираем числа от одного до n
# включительно. Число number умножается на очередное число, вычисляется
# следующий по порядку факториал. Результат помещается в список. По завершении
# цикла возвращаем список ответов.
def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result
for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

# Зарезервированное слово yield превращает функцию в
# генератор. Значение после yield возвращается из функции. Сама функция
# запоминает своё состояние: строку, на которой остановилось выполнение, значения
# локальных переменных. Повторный вызов функции продолжает работу с момента
# остановки.
# Изменим функцию для получения факториала чисел, превратив её в генератор.




def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number
for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))



def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)



for item in gen(10, 1):
    print(f'{item = }')
