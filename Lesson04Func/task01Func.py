def quadratic_equations(a: int | float, b: int | float, c: int | float) -> \
        tuple[
            float, float] | float | None:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:  # необязательно
        return None


print(quadratic_equations(2, -3, -9))


def no_mutable(a: int) -> int:
    a += 1
    print(
        f'In func {a = }')  # Для демонстрации работы, но не для привычки принтить
    # из функции
    return a


a = 42
print(f'In main {a = }')
z = no_mutable(a)
print(f'{a = }\t{z = }')

# Изменение списка внутри функции привело к изменению списка вне функции
def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }')
    return data


my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')

# Переменная a должна быть передана в обязательном порядке. Если не передать 2-й
# и/или 3-й аргумент, в переменные попадут нули как значения по умолчанию.
def quadratic_equations(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)

print(quadratic_equations(2, -9))


# Если в качестве значения по умолчанию нужен изменяемый тип данных,
# используют особый приём с None Если изменяемый объект не передан,
# он создаётся по новой для каждого вызова
# функции.
def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data


# ● Пример обычной функции:
def standard_arg(arg):
    print(arg)  # Принтим для примера, а не для привычки


standard_arg(42)
standard_arg(arg=42)


# Функция может принимать значения по позиции и по ключу. Мы явно указали имя
# переменной.


# ● Пример только позиционной функции:
def pos_only_arg(arg, /):
    print(arg)  # Принтим для примера, а не для привычки


pos_only_arg(42)


# pos_only_arg(arg=42) # TypeError: pos_only_arg() got some
# positional-only arguments passed as keyword arguments: 'arg'
# Теперь функция принимает только позиционные параметры.


# ● Пример только ключевой функции:
def kwd_only_arg(*, arg):
    print(arg)  # Принтим для примера, а не для привычки


# kwd_only_arg(42)
kwd_only_arg(arg=42)


# А теперь наоборот, можем принимать только значения по ключу.


# ● Пример функции со всеми вариантами параметров:
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard,
          kwd_only)  # Принтим для примера, а не для привычки


# combined_example(1, 2, 3)
# TypeError: combined_example() takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)


# combined_example(pos_only=1, standard=2, kwd_only=3)
# TypeError: combined_example() got some positional-only arguments
# passed as keyword arguments: 'pos_only'


def mean(args):
    return sum(args) / len(args)


print(mean([1, 2, 3]))


# print(mean(1, 2, 3)) # TypeError: mean() takes 1 positional argument but 3 were given

# функция принимает любое число позиционных аргументов. Переменная args
# превращается в кортеж. Можно сказать, что звёздочка упаковала все позиционные
# аргументы в один кортеж.

def mean(*args):
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))


# принимает ключевые параметры и
# возвращает словарь.
def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')


school_print(химия=5, физика=4, математика=5, физра=5)

# Обычно лямбды используют там, где однократно нужна функция и нет смысла
# заводить определение через def
my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(f'{s_key = }\n{s_value = }')
# В первом случае словарь сортируется по ключам, т.е. по алфавиту. Во втором
# благодаря лямбде указали сортировку по второму (индексация начинается с нуля)
# элементу, т.е. по значению.
