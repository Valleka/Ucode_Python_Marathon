import logging as l
#логер
logger = l.getLogger()
logger.setLevel(l.INFO)
#хендлер
handler = l.StreamHandler()
formatter = l.Formatter('%(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
#запись в файл
fn = l.FileHandler('shipments.log', mode='w')
fn.setFormatter(formatter)
logger.addHandler(fn)

class Ship:
    def __init__(self, route, containers):
        self.route = route
        self.containers = []
        self.add_containers(containers)
        logger.info(f"[Ship] initialized: {repr(self)}")
    def add_containers(self, containers2):
        for cont in containers2:
            if cont.cargo and cont.cargo.destination in self.route:
                self.containers.append(cont) #append() - добавляет элемент в конец списка.
                logger.info(f"[Ship] Added Container: {cont}")

    def __str__(self):
        buf = f"Ship to {self.route} with containers:"
        for cont in self.containers:
            buf += '\n' + str(cont)
        return buf

    def __repr__(self):
        return f"Ship(route={self.route}, containers={repr(self.containers)})"

class Container:
    def __init__(self, weight_limit: int, cargo=None):
        self.weight_limit = weight_limit
        if cargo and cargo.weight <= self.weight_limit:
            self.set_cargo(cargo)
        else:
            self.cargo = None
        logger.info(f"[Container] initialized: {self.__repr__()}")

    def set_cargo(self, cargo2):
        if cargo2.weight <= self.weight_limit:
            self.cargo = cargo2
            logger.info(f'[Container] Cargo set: {self.cargo}')
    def __str__(self):
        return f"Container up to {self.weight_limit} with {self.cargo}"
    def __repr__(self):
        return f"Container(weight_limit={self.weight_limit}, cargo={repr(self.cargo)})"

class Cargo:
    def __init__(self, destination: str, weight: int):
        self.destination = destination
        self.weight = weight
        logger.info(f'[Cargo] initialized: {self.__repr__()}')
    def __str__(self):
        return  f"Cargo to {self.destination} with weight {self.weight}"
    def __repr__(self):
        return f"Cargo(destination={self.destination}, weight={self.weight})"