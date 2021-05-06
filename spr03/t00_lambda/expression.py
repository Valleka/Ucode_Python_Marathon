n = int(input('n: '))
a = int(input('a: '))
b = int(input('b: '))

result = lambda n, a, b : n % a == 0 and n % b == 0

print(result(n, a, b))
