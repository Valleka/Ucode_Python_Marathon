import requests, re


def print_response(resp):
    #эту часть кода потом удалить
    # response = requests.get("https://google.com")
    # response.status_code
    #=====================

    st_code = str(resp.status_code)

    if st_code.startswith('2'):
        print(f"---Got response {resp.status_code} OK in {round(resp.elapsed.total_seconds(),2)} seconds---")
        print('---Response body---')
        print(resp.content)
        print()

    if st_code.startswith('4'):
        print(f"---Got response {resp.status_code} Not Found in {round(resp.elapsed.total_seconds(),2)} seconds---")

def print_history(reque):
