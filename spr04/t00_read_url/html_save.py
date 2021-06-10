import requests, re
from helper import print_stderr, print_stdout

def html_save(url, f_path):
    reg = r"^(https?|ftp|file)://.+$"
    res = re.search(reg, url)
    
    if res is not None:
        try:
            r = requests.get(url)
            print_stdout(f"Sending the request to the '{url}'.")
            print_stdout(f"Request to the '{url}' has been sent.")
            print_stdout(f"<Response [{r.status_code}]>.")
            print_stdout(f"Parsing page data.")
            print_stdout(f"Page data has been parsed.")
            try:
                print_stdout(f"Saving page data to '{f_path}'.")
                file = open(f_path, 'w')
                file.write(str(r.content))
                file.close
                print_stdout(f"Page data has been saved.")
            except Exception as e:
                print_stderr(e)
        except Exception as e:
            print_stderr(e)
    else:
        print_stderr("The site URL format is invalid.")
