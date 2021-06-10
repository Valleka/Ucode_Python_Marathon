from html_save import html_save


if __name__ == '__main__':

    print('*** Test 1 ***')
    html_save('https://www.bbc.com/', 'bbc.html')

    print('*** Test 2 ***')
    html_save('bbc.com', 'bbc.html')
