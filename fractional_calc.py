from fractions import Fraction as fr
global result


def fraction(number1, number2, operator):
    number1 = fr(number1)
    number2 = fr(number2)
    if operator in ('+', '-', '*', '/'):
        if operator == '+':
            result = number1 + number2
        elif operator == '-':
            result = number1 - number2
        elif operator == '*':
            result = number1 * number2
        elif operator == '/':
            result = number1 / number2
    if result.numerator > result.denominator:
        while result.numerator > result.denominator:
            find_whole_part = (result.numerator // result.denominator)
            find_numerator = result.numerator % result.denominator
            push_itog = f'{result} = {find_whole_part} {find_numerator}/{result.denomirator}'
            result = f'{number1} {operator} {number2} = {push_itog}'
            return result
    else:
        result = f'{number1} {operator} {number2} = {result}'
        return str(result)
