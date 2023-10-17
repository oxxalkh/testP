# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии

def sort_list(lst_: list[int]):
    for i in range(len(lst_)):
        for j in range(i, len(lst_)):
            if lst_[i] > lst_[j]:
                lst_[i], lst_[j] = lst_[j], lst_[i]


list_ = [83, 4, 65, 6, 14, 25, 678]
sort_list(list_)
print(list_)
