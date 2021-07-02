class Witch:
    #создаем екземпляр класса Witch, который создает объект с именем, для дальнейшего динамического создания
    # подклассов в классе Witch
    def __init__(self, name=None):
        self.name = name

def get_witch_class(class_name, specialty, skills):
    new_class = type(class_name, (Witch, ), dict(specialty=specialty))

    for func in skills:
        setattr(new_class, func.__name__, func)
    return new_class

