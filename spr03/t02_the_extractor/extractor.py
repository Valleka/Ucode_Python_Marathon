def extractor(extractable, value_type):
    dict_items = extractable.items() #перебираем словарь по ключу и значению и возвращаем итеррируемый объект
    tipe = lambda x : isinstance(x[1], value_type) #перебираем значения нашего словаря и проверяем тип данных и возвращаем тру или фолс
    
    res = dict(filter(tipe, dict_items)) #фильтруем только трушные объекты словаря и преобразовываем обратно в словарь
    
    return res
