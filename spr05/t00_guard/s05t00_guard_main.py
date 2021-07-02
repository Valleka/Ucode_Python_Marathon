from guard import Guard


if __name__ == "__main__":
    print(f'***EXAMPLE 1***')
    guard = Guard(name='Christopher')
    print(guard.greet())
    print(guard.receive_bribe(10))

    print(f'***EXAMPLE 2***')
    guard = Guard(salary=100)
    print(guard.greet())
    print(guard.receive_bribe(95))
    print(guard.receive_bribe(105))

    print(f'***EXAMPLE 3***')
    guard = Guard(name='Christopher', salary=100)
    print(guard.greet())
    print(guard.receive_bribe(80))
    print(guard.receive_bribe(135))
