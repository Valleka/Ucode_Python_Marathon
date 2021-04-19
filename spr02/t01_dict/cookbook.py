def search_cookbook(cookbook, recipe, section):
    if cookbook.get(recipe) != None:
        for buf in cookbook:
            if buf == recipe:
                res = cookbook[buf].get(section)
        if res != None:
            return res
        else:
            return f'There is no section "{section}" in the "{recipe}" recipe.'
    else:
        return f'There is no "{recipe}" recipe in the cookbook.'
