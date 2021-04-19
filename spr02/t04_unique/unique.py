def make_unique(args_d):
    for i in args_d:
        args_d[i] = sorted(list(set(args_d[i])))
    return args_d