class Knight:
    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg]) #записываем в объект self значение kwargs[arg] по ключу (имя атрибута) arg
    def greet(self):
        atr_name = hasattr(self, 'name') #возвращает тру, если поле name присутствует в словаре
        atr_title = hasattr(self, 'title')
        if atr_name and atr_title:
            print(f"Hello, I'm Sir {self.name} the {self.title}!")
        else:
            print("Hello!")