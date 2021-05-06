import json

def summary(filename, summarize_by):
    try:
        with open(filename, "w") as f:
            x = f.load()
            
    except:
        print(f'Error in decoding JSON.')
