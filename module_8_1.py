def add_everything_up(a, b):
    try:
        # Попытка сложить два числа
        result = a + b
        # Если сложение прошло успешно, возвращаем результат
        return result
    except TypeError:
        # Если возникла ошибка TypeError, значит a и b имеют разные типы
        # Возвращаем строковое представление этих двух данных вместе
        return str(a) + str(b)

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Результат: '123.456строка'
print(add_everything_up('яблоко', 4215))  # Результат: 'яблоко4215'
print(add_everything_up(123.456, 7))  # Результат: 130.456