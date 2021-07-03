from get_data import *
import logging as l

methods = {
    'get': lambda url: requests.get(url),
    'post': lambda url, data=None: requests.post(url, data),
    'put': lambda url, data=None: requests.put(url, data),
    'patch': lambda url, data=None: requests.patch(url, data),
    'delete': lambda url, data=None: requests.delete(url, data)
}

logger = l.getLogger()
logger.setLevel(l.INFO)
#хендлер
handler = l.StreamHandler()
formatter = l.Formatter('level: <%(levelname)s>: "%(message)s"')
handler.setFormatter(formatter)
logger.addHandler(handler)
#запись в файл
fn = l.FileHandler('shipments.log', mode='w')
fn.setFormatter(formatter)
logger.addHandler(fn)


if __name__ == '__main__':
    # logger = get_logger()
    logger.info("Getting args")
    args = get_parser()
    if not args.method:
        args.method = 'get'
    get_data(args, methods)