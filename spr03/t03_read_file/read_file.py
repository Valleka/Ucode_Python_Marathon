def read_file(f_read):
    try:
        f = open(f_read, 'r')
        f_data = f.read()
        print(f"File {f_read} has the following message:\n{f_data}")
    except:
        print(f'Failed to read file "{f_read}".')
