import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log(another_func):
    def wrapper(*args):
        buf = another_func(*args)
        logger.info(f"<{type(args[0]).__name__}>: - {another_func.__name__} method has been called.")
        return  buf
    return wrapper

class Ship:
    @log
    def __init__(self, route, containers):
        self.route = route
        self.containers = []
        self.add_containers(containers)

    @log
    def add_containers(self, containers2):
        for cont in containers2:
            if cont.cargo and cont.cargo.destination in self.route:
                self.containers.append(cont) #append() - добавляет элемент в конец списка.

    @log
    def __str__(self):
        buf = f"Ship to {self.route} with containers:"
        for cont in self.containers:
            buf += '\n' + str(cont)
        return buf

    @log
    def __repr__(self):
        return f"Ship(route={self.route}, containers={repr(self.containers)})"

class Container:
    @log
    def __init__(self, weight_limit: int, cargo=None):
        self.weight_limit = weight_limit
        self.set_cargo(cargo)

    @log
    def set_cargo(self, cargo2):
        if cargo2 and cargo2.weight <= self.weight_limit:
            self.cargo = cargo2
        else:
            self.cargo = None

    @log
    def __str__(self):
        return f"Container up to {self.weight_limit} with {self.cargo}"

    @log
    def __repr__(self):
        return f"Container(weight_limit={self.weight_limit}, cargo={repr(self.cargo)})"

class Cargo:
    @log
    def __init__(self, destination: str, weight: int):
        self.destination = destination
        self.weight = weight

    @log
    def __str__(self):
        return  f"Cargo to {self.destination} with weight {self.weight}"

    @log
    def __repr__(self):
        return f"Cargo(destination={self.destination}, weight={self.weight})"