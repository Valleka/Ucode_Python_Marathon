import sys
from string import ascii_uppercase
from redirect import Redirect


if __name__ == '__main__':
    path = 'test.txt'
    letter = iter(ascii_uppercase)
    print(next(letter), '[out]')
    print(next(letter), '[err]', file=sys.stderr)
    with Redirect(path, 'o'):
        print(next(letter), '[out]', 'in Redirect')
        print(next(letter), '[err]', 'in Redirect', file=sys.stderr)
    print(next(letter), '[out]')
    print(next(letter), '[err]', file=sys.stderr)
    with Redirect(path, 'e'):
        print(next(letter), '[out]', 'in Redirect')
        print(next(letter), '[err]', 'in Redirect', file=sys.stderr)
    print(next(letter), '[out]')
    print(next(letter), '[err]', file=sys.stderr)
    with Redirect(path, 'oe'):
        print(next(letter), '[out]', 'in Redirect')
        print(next(letter), '[err]', 'in Redirect', file=sys.stderr)
    print(next(letter), '[out]')
    print(next(letter), '[err]', file=sys.stderr)
