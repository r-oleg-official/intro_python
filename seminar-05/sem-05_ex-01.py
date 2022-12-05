# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# --> 'Я люблю абвЖвау иабв Питон'
# --> 'Я люблю Питон'
# включений, filter, map

# V.1.0.
my_string = 'Я люблю абвЖвау иабв Питон'
my_li = my_string.split()
my_li = list(filter(lambda el: not "абв" in el, my_li))
my_string = ' '.join(my_li)
print(my_string)

# V.1.1.
my_string = 'Я люблю абвЖвау иабв Питон'
my_li = my_string.split()
my_li = list(filter(lambda el: not "абв" in el, my_li))
my_string = ' '.join(my_li)
print(my_string)



