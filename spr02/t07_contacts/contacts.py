import re

def contacts(container, info, operation = ['add', 'update', 'delete']):
    in_name = r'^[a-zA-Z0-9-_ ]*$'
    in_mail = r'[^@]*@[^@]*\.[^@]*'
    
    if operation not in operation:
        return False
    if 'name' not in info or 'email' not in info:
        return False
    
    if re.match(in_mail, info['email']) is not None: #ищем входил ли in_mail в словаре info по ключу email
        if re.match(in_name, info['name']) is not None: # тоже самое по ключу name
            k = info.pop('email') # присвоил k почту, которую достал из аргумента info по ключу email
            
            if operation == 'add':
                container.update({k : info}) #обновляем словарь
                return True
            elif operation == 'update':
                if k in container:
                    container.update({k : {**container.get(k), **info}})
                    return True
                else:
                    return False
            else:
                if k in container:
                    container.pop(k, 'none') #удаляем элемент, который соответствует ключу k
                    return True
                else:
                    return False
            return False
        
    else:
        return False
    return True
