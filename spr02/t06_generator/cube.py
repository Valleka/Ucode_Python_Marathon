def cube(param):
    if param > 0:
        while param != 0:
            c_num = param ** 3
            yield c_num
            param -= 1