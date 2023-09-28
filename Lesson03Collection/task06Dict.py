a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
print(a == b == c)


# Для добавления в существующий словарь новой пары ключ-значение можно
# использовать обычную операцию присваивания.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
my_dict['ten'] = 10
print(my_dict)


TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict['two'])
print(my_dict[TEN])
#print(my_dict[1])  # KeyError: 1



# Если ли мы хотим гарантировать отсутствие ошибки KeyError при обращении к
# элементу словаря, можно обратиться к значению через метод get, а не квадратные
# скобки.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))
# Если обратиться к несуществующему ключу, get
# возвращает None. Метод get принимает второй аргумент, значение по умолчанию.
# Если ключ отсутствует в словаре, вместо None будет возвращено указанное
# значение.


my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')
# При вызове метода с одним аргументом отсутствующий ключ добавляется в
# словарь. В качестве значения передаётся None. Если указать два аргумента и ключ
# отсутствует, второй аргумент становится значением ключа и также добавляется в
# словарь. При обращении к существующему ключу, словарь не изменяется
# независимо от того указанные один или два аргумента.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())
for key in my_dict.keys():
    print(key)
# Обычно объект не используют напрямую. Метод keys применяется в связке с
# циклом for для перебора ключей словаря.


# Метод values похож на keys, но возвращает значения в виде объекта итератора
# dict_values, а не ключи.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())
for value in my_dict.values():
    print(value)


# Если в цикле необходимо работать одновременно с ключами и значениями, как с
# парами, используют метод items.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())

for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')


my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')


# Метод pop удаляет пару ключ-значение по переданному ключу.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
# err = my_dict.pop('six')
# KeyError: 'six'
# err = my_dict.pop()
# TypeError: pop expected at least 1 argument, got 0

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)
# На вход метод получает другой словарь в любой из вариаций создания словаря.
# Если передать существующий ключ, значение будет заменено новым.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'rat': 'крыса'}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)
# При перезаписи совпадающих ключей приоритет отдаётся словарю,
# расположенному правее.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.setdefault('ten', 555))
print(my_dict.values())
print(my_dict.pop('one'))
my_dict['one'] = my_dict['four']
print(my_dict)


