import itertools 

def group(test_case_data, key):

    group = {}

    key_f = lambda x : x[2]

    for k, group in itertools.groupby(test_case_data, key_f):
        print(k)
        print(str(group))