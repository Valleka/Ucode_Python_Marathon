import re

def check_address2(args):
    buf = r'^Ukraine,[ ]*[A-Za-z-[ ]*]*,[ ]*[A-Za-z-[ ]*]*[ ]*\d{1,6},[ ]*\d{5}$'
    res = []
    for i in args:
        if re.match(buf, args[i]) is not None:
            res.append(f"The address of {i} is valid.")
        else:
            res.append(f"The address of {i} is invalid.")
    return res



def check_address(dict):
    tpl = r'^Ukraine,[ ]*[A-Za-z-[ ]*]*,[ ]*[A-Za-z-[ ]*]*[ ]*\d{1,6},[ ]*\d{5}$'
    res = []
    for it in dict:
        if re.match(tpl, dict[it]) is not None:
            res.append(f'The address of {it} is valid.')
        else:
            res.append(f'The address of {it} is invalid.')
    return res