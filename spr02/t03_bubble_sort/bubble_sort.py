def bubble_sort(args):
    sort = True
    while sort:
        sort = False
        for i in range(len(args) - 1):
            if args[i] > args[i + 1]:
                args[i], args[i + 1] = args[i + 1], args[i]
                sort = True
    return args