# ● Метод tell
# Метод tell возвращает текущую позицию в файле.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data1.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())


# ● Метод tell
# Метод tell возвращает текущую позицию в файле

last = before = 0
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data1.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))
print('1')

# ● Метод seek
# Метод seek позволяет изменить положение “курсора” в файле.
# seek(offset, whence=0), где offset — смещение относительно опорной точки, whence -
# способ выбора опороной точки.
# ● whence = 0 - отсчёт от начала файла
# ● whence = 1 - отсчёт от текущей позиции в файле
# ● whence = 2 - отсчёт от конца файла
# 🔥 Важно! Значения 1 и 2 допустимы только для работы с бинарными
# файлами. Исключение seek(0, 2) для перехода в конец текстового файла.
# Метод возвращает новую позицию “курсора”.
last = before = 0
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))

print('2')
# ● Метод truncate
# truncate(size=None) — метод изменяет размер файла. Если не передать значение в
# параметр size будет удалена часть файла от текущей позиции до конца. Метод
# возвращает позицию после изменения файла.

last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f.seek(before, 0))
    print(f.truncate())

print(3)
# Если передать параметр size метод изменяет размер файла до указанного числа
# символов или байт от начала файла.
size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))
print(4)