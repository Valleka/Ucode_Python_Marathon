import json
import yaml

dct = {
    "json": lambda path: json.loads(path),
    "yaml": lambda path: yaml.safe_load(path),
}


def to_file(path: str, extension: str):
    try:
        print(path)
        with open(path, 'r') as f:
            file = f.read()
            line = dct[extension](file)
    except Exception:
        print('error')
        return None
    return line


def get_data(path, extension):
    if type(path) != str:
        return None
    if extension in dct:
        try:
            pth = path.split(f'.{extension}')
            if len(pth) == 2:
                return to_file(path, extension)
            else:
                pth = path + '.' + extension
                return to_file(pth, extension)
        except json.JSONDecodeError:
            return None
        except yaml.YAMLError:
            return None
    else:
        return None
