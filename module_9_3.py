# генераторные сборки

first =  ['Strings', 'Student', 'Computers']
second = ['Строка',  'Урбан',   'Компьютер']

# В переменную first_result запиcана генераторную сборка, которая высчитывает разницу длин строк
# из списков first и second, если их длины не равны.
# Для перебора строк попарно из двух списков используется функция zip.
first_result = (abs(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))

# В переменную second_result записывается генераторная сборка, которая содержит результаты
# сравнения длин строк в одинаковых позициях из списков first и second.
# Эта сборка НЕ использует функцию zip.
second_result = (True if len(first[i]) == len(second[i]) else False for i in range(len(first)))

print(list(first_result))
print(list(second_result))