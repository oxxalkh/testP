a, b, c = ("один", "два", "три",)
print(f'{a=} {b=} {c=}')


# ● Распаковка коллекции с упаковкой “лишнего”, упаковка со звёздочкой
# Для упаковки может применяться символ “звёздочка” перед именем переменной.
# Такая переменная превратиться в список и соберёт в себя все значения, не
# поместившиеся в остальные переменные.

data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')


a = b = c = 0
a += 42
print(f'{a=} {b=} {c=}')

# ● Множественное присваивание
# Если несколько переменных должны получить одинаковые значение, можно
# объединить несколько строк в одну.
a = b = c = {1, 2, 3}
a.add(42)
print(f'{a=} {b=} {c=}')


a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')

t = 1, 2, 3
print(f'{t=}, {type(t)}')




