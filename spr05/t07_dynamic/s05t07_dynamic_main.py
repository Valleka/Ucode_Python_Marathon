from witch_maker import get_witch_class


# function to test a created class and its instance
def test(my_class, instance):
    # get __dict__ of class without special methods and attributes
    class_dict = list(filter(lambda x: not x[0].startswith('__'),
                             my_class.__dict__.items()))
    methods = list(filter(lambda x: callable(x[1]), class_dict))
    print(f'class {my_class.__name__} ({my_class.__base__.__name__})')
    print('class __dict__:', *class_dict)
    print('instance __dict__:', instance.__dict__)
    for method_name, method in methods:
        print(f'Calling method "{method_name}": ', end='')
        getattr(instance, method_name)()
    print('---')


# functions that will be added to 'skills'
def control_tides(self):
    print(f'{self.name} is controlling the tides.')


def read_tarot(self):
    print(f'{self.name} is reading tarot cards.')


def palmistry(self):
    print(f'{self.name} is palm reading.')


def conjure_dead(self):
    print(f'{self.name} is conjuring the spirits of the dead.')


if __name__ == "__main__":
    NoSkillWitch = get_witch_class('NoSkillWitch', None, [])
    test(NoSkillWitch, NoSkillWitch('Diana'))

    SeaWitch = get_witch_class('SeaWitch', 'water magic', [control_tides])
    test(SeaWitch, SeaWitch('Calypso'))

    DivinationWitch = get_witch_class('DivinationWitch', 'fortune telling',
                                      [read_tarot, palmistry])
    test(DivinationWitch, DivinationWitch('Ada'))

    Necromancer = get_witch_class('Necromancer', 'the dead', [conjure_dead])
    test(Necromancer, Necromancer('the Witch of Endor'))

    TestWitch = get_witch_class('L', 'lambda methods',
                                [lambda self:
                                 print(f'{self.name} is in lambda.')])
    test(TestWitch, TestWitch('Ella'))
