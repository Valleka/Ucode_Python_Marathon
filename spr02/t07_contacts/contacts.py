import re

def contacts(container, info, operation = ['add', 'update', 'delete']):
    if operation not in operation:
        return False
    if 'name' not in info or 'email' not in info:
        return False
    
    in_name = r'^[a-zA-Z0-9-_ ]*$'
    in_mail = r'[^@]*@[^@]*\.[^@]*'
    
    
    
    
    
