def witch_hunt(suspect_sets, innocent_sets):
    witch_set = set()
    
    if suspect_sets:
        witch_set = suspect_sets[0].intersection(*suspect_sets)
    witch_set = witch_set.difference(*innocent_sets)
    
    return witch_set