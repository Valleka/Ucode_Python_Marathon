import logging, sys

#логер
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#декоратор
def log(another_func):
    def wrapper(*args, **kwargs):
        logger.info(f"{another_func.__name__} with {kwargs}")
        return  another_func(*args, **kwargs)
    return wrapper

class Knight:
    i = 0
    instances = []
    @log
    def __new__(cls, **kwargs):

        if cls.i > 3:
            logger.error("Cannot create a Knight. The Round Table can only fit 4 Knights.")
            return None
        if kwargs.get('name') == 'Arthur':

            logger.error("Cannot create a Knight with the name Arthur. Arthur is the King.")
            return None
        for arg_key, arg_value in kwargs.items():
            setattr(cls, arg_key, arg_value)
            cls.i += 1
            return object.__new__(cls)

    @log
    def __init__(self, **kwargs):
        for arg_key, arg_value in kwargs.items():
            setattr(self, arg_key, arg_value) #передаем в объект self значение arg_value по ключу (имя атрибута) arg_key
        self.instances.append(self)