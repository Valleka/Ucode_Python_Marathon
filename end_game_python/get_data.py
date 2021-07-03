import argparse
import requests

from endgame import logger
from print_data import print_response


def get_parser():
    try:
        parser = argparse.ArgumentParser(description="Work with api")
        parser.add_argument('--method', type=str, help='Method for work with api')
        parser.add_argument('--endpoint', type=str, help='Url of api')
        parser.add_argument('--params', type=list, nargs='+', help='Parameters for query to api')
        parser.add_argument('--headers', type=list, nargs='+', help='Headers of query to api')
        parser.add_argument('--body', type=list, nargs='+', help='Body of query to api')
        parser.add_argument('--auth', type=list, nargs='+', help='specify username and password for Basic Authentication')
        logger.info('Args parsed')
        return parser.parse_args()
    except argparse.ArgumentError and argparse.ArgumentTypeError as err:
        logger.error(err)


def make_param(params):
    dct = dict()
    for p in params:
        dct[p[0]] = p[2]
    return dct


def get_data(args, methods='get'):
    try:
        if args.endpoint:
            if args.method in methods:
                if args.params:
                    logger.info('Get data from args')
                    data = make_param(args.params)
                    logger.info('Sending request')
                    response = methods[args.method](args.endpoint, data)
                    print_response(response)
                    logger.info(f'Recieved data with status {response.status_code}')
                else:
                    logger.info('Sending request')
                    response = methods[args.method](args.endpoint)
                    print_response(response)
                    logger.info(f'Recieved data with status {response.status_code}')
                return response
    except requests.RequestException as e:
        logger.error(e)