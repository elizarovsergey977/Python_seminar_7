from complex_calc import arifmetics
from fractional_calc import fraction
from logging import logger

words1 = {0: 'Действительную часть', 1: 'Мнимую часть'}
words2 = {0: 'Числитель', 1: 'Знаменатель'}
num1 = list()


def validation(a):
    try:
        int(a)
        return True
    except:
        print('Введены неверные данные')
        return False


print('Калькулятор работает .....\n'
      'Выберите тип вычисления :\n'
      '1) Операции с комплексными числами\n'
      '2) Операции с дробями\n')
mode = input()
if validation(mode):
    print('Введите необходимые действия :\n')
    global mode1
    mode1 = input()
    if mode1 not in '+-*/':
        print('Введены некорректные данные\n'
              'Окончание работы программы')
    elif mode == '1':
        c = 1
        print('Выбран режим вычисления комлексных чисел\n')
        for i in range(2):
            for j in range(2):
                print(f'Введите {words1[j]} числа {[i + 1]}\n')
                buffer = input()
                validation(buffer)
                if validation(buffer):
                    num1.append(int(buffer))
                else:
                    print('Введены некорректные данные\n')
                    break
        num2 = [num1[2], num1[3], mode1]
        num1.pop()
        num1.pop()
        res = arifmetics(num1, num2, mode1)
        logger(res)
        print(res)
    elif mode == '2':
        print('Выбран режим вычисления натуральных дробей\n')
        for i in range(2):
            for j in range(2):
                print(f'Введите {words2[j]} числа {[i + 1]}\n')
                buffer = input()
                validation(buffer)
                if validation(buffer):
                    num1.append(int(buffer))
                else:
                    print('Введены некорректные данные\n')
                    break
        num2 = [num1[2], num1[3], mode1]
        num1.pop()
        num1.pop()
        res = fraction(f'{num1[0]}/{num1[1]}',f'{num2[0]}/{num2[1]}', mode1)
        logger(res)
        print(res)
    else:
        print('Выбранный режим не определен\n')
else:
    print('Окончание работы программы')
