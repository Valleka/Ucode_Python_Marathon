operations = {
    'add' : lambda x, y : x + y,
    'sub' : lambda x, y : x - y,
    'mul' : lambda x, y : x * y,
    'div' : lambda x, y : x / y,
    'pow' : lambda x, y : x ** y
}

def calculator(operator, num_1, num_2):
    if operator not in operations:
        raise ValueError('Invalid operation. Available operations: add, sub, mul, div, pow')
    if (type(num_1) != int and type(num_1) != float) or (type(num_2) != int and type(num_2) != float):
        raise ValueError("Invalid numbers. Second and third arguments must be numerical")
    else:
        return operations.get(operator)(num_1, num_2)
