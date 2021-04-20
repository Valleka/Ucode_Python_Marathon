from cube import cube


if __name__ == '__main__':
    n = 3
    print(f'***Passed parameter - {n}***')
    for i in cube(n):
        print(i)
    print('***')

    n = 8
    print(f'***Passed parameter - {n}***')
    for i in cube(n):
        print(i)
    print('***')

    n = 10
    print(f'***Passed parameter - {n}***')
    for i in cube(n):
        print(i)
    print('***')

    n = 0
    print(f'***Passed parameter - {n}***')
    for i in cube(n):
        print(i)
    print('***')

    n = -5
    print(f'***Passed parameter - {n}***')
    for i in cube(n):
        print(i)
    print('***')
