# Помимо обычного импорта можно использовать более подробную форму записи.
# Зарезервированное слово from указывает на имя модуля или пакета, далее import и
# имена импортируемых объектов.
from sys import builtin_module_names, path
print(builtin_module_names)
print(*path, sep='\n')
