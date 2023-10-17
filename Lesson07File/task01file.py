
'''
Режимы работы с файлами
Рассмотрим доступные режимы работы с файлами.
➢ 'r' — открыть для чтения (по умолчанию)
➢ 'w' — открыть для записи, предварительно очистив файл
➢ 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже
существует
➢ 'a' — открыть для записи в конец файла, если он существует
➢ 'b' — двоичный режим
➢ 't' — текстовый режим (по умолчанию)
➢ '+' — открыты для обновления (чтение и запись)
'''

f = open('text_data.txt', 'r', encoding='utf-8')
print(f)
print(list(f))

f = open('text_data.txt', 'a', encoding='utf-8')
f.write('Окончание файла \n')
f.close()

f = open('bin_data', 'wb', buffering=64)
f.write(b'X' * 1200)
f.close()

f = open('data.txt', 'wb')
f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
f.close()
# f = open('data.txt', 'r', encoding='utf-8')
# print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode
# # byte 0xec in position 14: invalid continuation byte
# f.close()
f = open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()
