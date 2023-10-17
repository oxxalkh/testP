with (
    open('text_data.txt', 'r+', encoding='utf-8') as f1,
    open('bin_data', 'rb') as f2,
    open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3):
    print(list(f1))
    print(list(f2))
    print(list(f3))

# ● Чтение в список
with open('text_data.txt', 'r', encoding='utf-8') as f:
    print(list(f))

''' 
 ● Чтение методом read
read(n=-1) — читает n символов или n байт информации из файла. Если n
отрицательное или не указана, читает весь файл. Попытка чтения будет даже в том
случае, когда файл больше оперативной памяти.
 
'''

with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}')

''' 
При чтении файла блоками фиксированного размера можно воспользоваться
циклом while. Дочитав до конца в переменную попадёт пустая строка, которая в
цикле будет интерпретирована как ложь и завершит тело цикла.
'''
SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)

'''
● Чтение методом readline
Для чтения текстового файла построчно используют метод readline.
'''

with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)

# ● Чтение циклом for
# Вместо метода readline без аргумента можно использовать более короткую запись с
# циклом for
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
