def witch_hunt(suspect_sets, innocent_sets):
    #sus_set = set(suspect_sets)
    #inn_set = set(innocent_sets)
    #witch_set = sus_set.intersection(inn_set)
    #l_s = len(suspect_sets)
    #l_i = len(innocent_sets)
    #s = 0
    #i = 0
    
    witch_set = set()
    
    if suspect_sets:
        witch_set = suspect_sets[0].intersection(*suspect_sets)
    witch_set = witch_set.difference(*innocent_sets)
    
    return witch_set
    
    
    #while s < l_s:
    #    sus_set = suspect_sets[0].difference(suspect_sets[s])
    #    s += 1
        
    #while i < l_i:
    #    inn_set = innocent_sets[0].difference(innocent_sets[i])
    #    i += 1
        
    #witch_set = sus_set.intersection(inn_set)
    
    #return witch_set
