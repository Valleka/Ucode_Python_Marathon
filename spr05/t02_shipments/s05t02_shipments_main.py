import random
import sys
from shipments import Cargo, Container, Ship


def to_set():
    return random.randint(0, 1)


if __name__ == '__main__':
    random.seed(sys.argv[1])  # set seed in command line
    destinations = ['Tianjin', 'Antwerp', 'Los Angeles', 'Xiamen', 'Bremen',
                    'Santos', 'Barcelona']
    containers = []
    # creating random cargo and containers
    for i in range(16):
        destination = random.choice(destinations)
        weight = random.randint(1000, 3000)
        weight_limit = random.randint(1000, 4000)
        cargo = Cargo(destination, weight)
        print(cargo)
        # setting cargo either in __init__ or in method directly
        if to_set():
            container = Container(weight_limit, cargo)
        else:
            container = Container(weight_limit)
            container.set_cargo(cargo)
        print(container)
        containers.append(container)

    # creating a ship with a random route and the created containers
    route = random.sample(destinations, 3)
    # adding part of the containers in the __init__
    ship = Ship(route, containers[:8])
    # part with method directly
    ship.add_containers(containers[8:])
    print(ship)
