from knight import Knight


if __name__ == '__main__':
    Knight(name='Robin', title='Not-quite-so-brave-as-Sir-Lancelot',
           deed='Nearly fought the Dragon of Angnor.')
    Knight(name='Arthur', age=25)
    Knight(name='Aban', height=150)
    Knight(name='Ector', title='Responsible')
    Knight(name='Galahad')
    Knight(title='Brave', skill='archery')
    Knight(name='Tristan')
    Knight(name='Arthur')
    for i in Knight.instances:
        print(i.__dict__)
