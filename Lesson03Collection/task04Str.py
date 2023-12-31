# Индексы и срезы работают аналогично спискам.
text = 'Hello world!'
print(text[6])
print(text[3:7])
# Если необходимо заменить элемент новым, индексы не подойдут. Для этих целей
# нужен метод replace
# Первый аргумент — подстрока, которую нужно заменить.
# Второй аргумент — подстрока, на которую нужно заменить.
# Третий аргумент — максимальное количество замен. Если его не указывать, будут
# заменены все совпадения.
new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')

# строка поддерживает методы count для подсчёта вхождения и index
# для поиска элемента. Но у строки появился и новый метод find. Он работает
# аналогично index. Но если искомая подстрока отсутствует, вместо ошибки
# возвращает -1.
text = 'Hello world!'
print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))

# Для разворота строки используется обратный срез, как и в случае со списком.
text = 'Hello world!'
print(text[::-1])


# f - format
name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)
print(text)

pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')
num = 2 * pi * data[1]
print(f'{num = :_}')

# :.2f — число пи выводим с точность два знака после запятой
# ● :>10 — элементы списка выводятся с выравниванием по правому краю и
# общей шириной вывода в 10 символов
# ● = — выводим имя переменной, знак равенства с пробелами до и после него и
# только потом значение.
# ● :_ — число разделяется символом подчёркивания для деления на блоки по 3
# цифры.


# Метод split позволяет разбить строку на отдельные элементы в соответствии с
# разделителем и поместить результат в список.
link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/')
print(urls)
a, b, c = input('Введите 3 числа через пробел: ').split()
print(c, b, a)

# Один из способов избежать ошибки лишних (но не меньших) данных при
# распаковке методом split — использовать символ распаковки.
a, b, c, *_ = input('Введите не менее трёх чисел через пробел: ').split()

# Метод join принимает на вход итерируемую последовательность и соединяет все её
# элементы в строку, разделяя каждый текстом, к которому применён метод. В
# некоторой степени join противоположен split.
data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1',
'posts']
url = '/'.join(data)
print(url)

text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
# ● upper — все символы приводятся к верхнему регистру
# ● lower — все символы приводятся к нижнему регистру
# ● title — первый символ каждого слова (разделитель слов - пробел) приводится
# к верхнему регистру, остальные символы к нижнему
# ● capitalize — первый символ строки в верхнем регистре, остальные в нижнем


# Метод startswith проверяет начинается ли строка с заданной подстроки. Метод
# возвращает истину или ложь. Метод endswith проверяет окончание строки
# переданной в качестве аргумента подстрокой.
text = 'Однажды в студёную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))

text = 'Привет, мир!'
print(text.find(' '))
print(text.title())
print(text.split())
print(f'{text = :>25}')


