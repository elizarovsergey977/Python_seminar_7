def arifmetics(a, b, znak):
    comp_number1 = complex(a[0], a[1])
    comp_number2 = complex(b[0], b[1])
    operator = {'+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y}
    result = f'{comp_number1} {znak} {comp_number2} = {operator[znak](comp_number1, comp_number2)}'
    return result
