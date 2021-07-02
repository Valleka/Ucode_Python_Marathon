class Guard:
    def __init__(self, **args):
        if len(args) == 2:
            self.name = args['name']
            self.salary = args['salary']
        elif len(args) == 1:
            if 'name' in args:
                self.name = args['name']
                self.salary = 0
            elif 'salary' in args:
                self.name = None
                self.salary = args['salary']
        else:
            self.name = None
            self.salary = 0

    def greet(self):
        return f"Hello, my name is {self.name}!"

    def receive_bribe(self, summ):
        if self.salary < summ:
            return f"You may pass."
        else:
            return f"I am not letting you pass."

