# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# def ord_txt(n: str) -> list[int]:
#     b = set()
#     for el in n:
#         b.add(ord(el))
#     return sorted(list(set(b)), reverse=True)

def ord_txt(n: str) -> list[int]:
    return sorted(list(set(map(ord, list(n)))), reverse=True)


text_n = input()
print(ord_txt(text_n))
