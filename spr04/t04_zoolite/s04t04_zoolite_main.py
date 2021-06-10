from zoolite import update_zoo
import json
import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as data_file:
        update_zoo(data=json.load(data_file))
