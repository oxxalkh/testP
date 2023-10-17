# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

# for i in range(2, 10):
#     for j in range(2, 11):
#         print(f"{i} x {j} = {i*j}", end="\t")
#     print()


# for i in range(2, 10, 4):
#     for j in range(2, 11):
#         for k in range(i, i+4):
#             print(f"{k:>3} x {j:>3} = {(k * j):>3}", end="\t")
#         print()
#     print()
#
# res = [f"{k:>3} x {j:>3} = {(k * j):>3}" for j in range(2,11)
# for i in range(2, 10, 4) for k in range(i, i + 4)]
#

result = [print(f"{i} x {j} = {i*j}", end="\t")
       if j != 10
       else print(f"{i} x {j} = {i*j}")
       for i in range(2, 10)
       for j in range(2, 11)]

res_1 = [f'{k:>3} *{j:>3} ={(k * j):>3}' for i in range(2, 10, 4) for j in range(2, 11) for k in range(i, i + 4)]

res_2 = ['\n'+'\t'.join([f'{k:>3} *{j:>3} ={(k * j):>3}'
                         for k in range(i, i + 4)])
         if i == 6 and j == 2 else '\t'.join([f'{k:>3} *{j:>3} ={(k * j):>3}'
                                              for k in range(i, i + 4)])
         for i in range(2, 10, 4)
         for j in range(2, 11)]

# print('\t'.join(res))


print(*res_2, sep='\n')