# создание функций "на лету"

# 1. Lambda-функция:
# Даны 2 строки.
# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.
# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.

first = 'Мама мыла раму'
second = 'Рамена мало было'

res = list(map(lambda x, y: True if x == y else False, first, second))
print(res)

# 2. Замыкание:
# get_advanced_writer(file_name) принимает название файла для записи.
# Внутри этой функции, написана ещё одна - write_everything(*data_set),
# где *data_set - параметр принимающий неограниченное количество данных любого типа.
# Логика write_everything заключается в добавлении в файл file_name всех данных
# из data_set в том же виде.
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            # list() нужно чтобы ленивая функция map сработала
            list(map(lambda data: file.write(str(data) + '\n'), data_set))
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# 3. Метод __call__:
# класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе также определен метод __call__, который случайным образом выбирает слово
# из words и возвращает его. Для случайного выбора с одинаковой вероятностью для каждого
# данного в коллекции используется функция choice из модуля random.
import random

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())