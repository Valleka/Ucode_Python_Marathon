import functools

def multiplier(list_num):
    res = lambda a, b: a * b
    
    if (type(list_num) == list) and all(isinstance(dict_items,(int, float)) for dict_items in list_num):
        return functools.reduce(res, list_num)
    else:
        raise ValueError("The given data is invalid.")
