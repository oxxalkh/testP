my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)
rev_list = list(reversed(my_list))
print(rev_list)

for item in reversed(my_list):
    print(item)

my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print(my_list)

