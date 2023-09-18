very_long_text = 'Lorem ipsum dolor sit amet, consectetur' \
                 'adipisicing elit. A ab alias animi assumenda at aut ' \
                 'commodi, consequatur cumque ea harum, hic id illum ipsam itaque laboriosam magnam minus nam nulla ' \
                 'numquam obcaecati officia officiis porro possimus praesentium quaerat temporibus ullam veniam? '
print(very_long_text)

LIMIT = 120
ATTENTION = 'Внимание!'
name = input('Твоё имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) + \
       " до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов.'
print(text)

empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())
