from decorator import Cargo, Container, Ship

if __name__ == '__main__':
    cargos = [Cargo('Hamburg', 1200),
              Cargo('Kaohsiung', 700),
              Cargo('Hamburg', 8000),
              Cargo('Manila', 1500)]

    containers = [Container(1000, cargos[0]),
                  Container(3000, cargos[1]),
                  Container(10000, cargos[2]),
                  Container(2000)]
    containers[3].set_cargo(cargos[3])

    ship = Ship(['Manila', 'Hamburg', 'Fuzhou', 'Piraeus', 'Kaohsiung'],
                containers)
    ship.add_containers([Container(3000, Cargo('Hamburg', 3000))])

    print('\n*** Ship __str__ ***')
    print(ship)
    print('\n*** Ship __repr__ ***')
    print(repr(ship))
