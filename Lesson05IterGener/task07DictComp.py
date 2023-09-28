my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')
#  качестве выражения для добавления
# указываются две переменные через двоеточие: key: value.

data = {2, 4, 4, 5, 5, 5, 6, 8, 10, 12}
res1 = {None: item + 1 for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]
print(type(res1), res1, res2, res3)

