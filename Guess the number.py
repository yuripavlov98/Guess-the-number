import random  # подключаем модуль

number = random.randint(1, 101)  # генерируем случайное число от 1 до 100

print('Добро пожаловать в числовую угадайку')


def is_valid(num):  # функция проверки введенных данных на корректность
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False
