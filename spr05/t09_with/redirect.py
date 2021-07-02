import sys

class Redirect:
    def __init__(self, path, dir):
        self.path = path
        self.dir = dir
        self.o = sys.stdout
        self.e = sys.stderr

    def __enter__(self):
        self.file = open(self.path, 'a')
        if self.dir == 'o':
            sys.stdout = self.file
        if self.dir == 'e':
            sys.stderr = self.file
        if self.dir == 'oe':
            sys.stdout = self.file
            sys.stderr = self.file
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            print('exit exception text: %s' % exc_value)
            return True
        sys.stdout = self.o
        sys.stderr = self.e
        self.file.close()




