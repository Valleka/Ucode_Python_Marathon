from gadgets import Phone, Computer, Smartphone, IPhone


def test_instance(instance):
    print(instance.__class__)
    print(*instance.__dict__.items(), sep='\n')
    if hasattr(instance, 'make_call'):
        instance.make_call('+380 72 384 4834')
    print('-')


if __name__ == '__main__':
    phone = Phone(number='+380 50 709 3941')
    test_instance(phone)
    computer = Computer(operating_system='Windows 10',
                        cpu='Intel Core i7',
                        ram_size=16,
                        input_devices=['keyboard', 'mouse'])
    test_instance(computer)
    smartphone = Smartphone(operating_system='Android',
                            cpu='Octa-core',
                            ram_size=8,
                            number='+380 73 472 8879',
                            battery=4500)
    test_instance(smartphone)
    iphone = IPhone(cpu='Hexa-core',
                    ram_size=6,
                    number='+380 95 843 8467',
                    battery=2815)
    test_instance(iphone)
