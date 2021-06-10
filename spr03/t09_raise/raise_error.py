def raise_error(key, mes):
    if key == 'value':
        raise ValueError(mes)
    elif key == 'key':
        raise KeyError(mes)
    elif key == 'index':
        raise IndexError(mes)
    elif key == 'memory':
        raise MemoryError(mes)
    elif key == 'name':
        raise NameError(mes)
    elif key == 'eof':
        raise EOFError(mes)
    else:
        raise ValueError('No error with such key.')