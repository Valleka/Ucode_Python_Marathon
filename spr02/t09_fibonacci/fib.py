def fib(fib_num):
    n1, n2 = 0, 1
    i = 0
    
    if  fib_num == 1:
        return n1
    else:
        while i < fib_num:
            n1, n2 = n2, n1 + n2
            i += 1
        return n1
    
    

def fib_generator(fib_num):
    n1, n2 = 0, 1
    i = 0

    if fib_num == 1:
        yield n1
    else:
        while i < fib_num:
            yield n1
            n1, n2 = n2, n1 + n2
            i += 1
