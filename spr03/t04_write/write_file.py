def write_file(filename, mess_add = None):
    if filename.endswith('.txt') == True:
        with open(filename, 'w') as f:
            if mess_add is not None:
                if f.write(mess_add) is not None:
                    print(f'Your message has been written to file "{filename}".')
                    print(f'File "{filename}" now contains the following text:\n{mess_add}')
                else:
                    print("Something went wrong...")
            else:
                print(f'Your message has been written to file "{filename}".')
                print(f'File "{filename}" now contains the following text:\nNone')
    else:
        print('Please enter the filename in the format "filename.txt".')
        print(f'Failed to write to file "{filename}".')
