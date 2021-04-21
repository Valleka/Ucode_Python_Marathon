def contains(my_str, sub_str):
    res_str = []
    my_str = my_str.lower()
    
    for i in sub_str:
        if my_str.find(i) != -1:
            res_str.append(i)
    return res_str