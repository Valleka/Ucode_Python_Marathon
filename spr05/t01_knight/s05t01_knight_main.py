import json
from knight import Knight


if __name__ == '__main__':
    knights = [
        Knight(
            name='Robin',
            title='Not-quite-so-brave-as-Sir-Lancelot',
            deeds=['Nearly fought the Dragon of Angnor.',
                   'Nearly stood up to the vicious Chicken of Bristol.',
                   'Personally wet himself at the Battle of Badon Hill.'],
            group='Knights of the Round Table',
            gender='male'),
        Knight(name='Bedevere'),
        Knight(eyes='brown', age=30)
    ]

    for knight in knights:
        print(json.dumps(knight.__dict__, indent=1))
        knight.greet()
        print('---')
