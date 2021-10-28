"""
Netology. Derarators.

1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы,
   с которыми вызвалась и возвращаемое значение.
2. Написать декоратор из п.1, но с параметром – путь к логам.
3. Применить написанный логгер к приложению из любого предыдущего д/з.
"""
from datetime import datetime
a, b = 3, 5
path = 'files/log.txt'


def parametrized_decor(file_path):
    def decorator(func):
        """
        Функция декоратор принимает другую функцию,принимает путь для записи лога, записывает в файл дату и
        время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
        :param func:
        :return:
        """
        info = {}

        def wrapper(*args, **kwargs):
            '''
            Декоратор
            :param file_path_:
            :param args:
            :return:
            '''
            date_time = datetime.now().strftime("%d %b %Y, %H : %M : %S")
            result = func(*args, **kwargs)
            #  Обертка принимает функцию для обработки
            info['Дата и время вызова функции: '] = date_time
            info['Имя функции: '] = func.__name__
            info['Аргументы функции: '] = args
            info['Файл лога: '] = file_path
            info['Возвращаемое значение: '] = result
            with open(file_path, 'a', encoding="UTF-8") as f:
                for key, value in info.items():
                    f.write(f'{key} {value}\n')
                f.write('-' * 50 + '\n')
            print(f'Данные функции {func.__name__} записаны в файл {file_path}')
            return result
            #  Обертка возвращает результат работы принятой функции
        return wrapper
    return decorator


@parametrized_decor(path)
def multiply(a_, b_):
    m = a_ * b_
    return m


multiply(a, b)
