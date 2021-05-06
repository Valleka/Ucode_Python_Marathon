import re

def clear_words(str_text):
    simb = r' |\?|!|\.|:|;|,|-'
    arr_spl = re.split(simb, str_text)
    res = list(filter(None, map(lambda x : str.strip(x), arr_spl)))
    
    return res