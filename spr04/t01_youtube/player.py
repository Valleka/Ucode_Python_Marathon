import re, sys, webbrowser

from helper import print_stderr, print_stdout

try:
    url = sys.argv[1]
    reg = r"^(https?|ftp|file)://.+$"
    res = re.search(reg, url)

    if res is not None:
        if 'youtube.com' in url:
            try:
                print_stdout(f"Opening the YouTube video at {url}.")
                webbrowser.open(url)
                print_stdout(f"YouTube video opened.")
            except Exception as e:
                print_stderr(e)
        else:
            print_stderr("The URL is invalid.")
    else:
        print_stderr("The URL is invalid.")
except Exception:
    print_stderr("The site URL was not passed.")
