import requests
import json

def get_json(href):
    session = requests.Session()
    session.trust_env = False
    r = session.get(href)
    r = json.loads(r.text)
    return r


def download_file(filename, href):
    session = requests.Session()
    session.trust_env = False
    r = session.get(href)
    with open(filename, 'wb') as fn:
        fn.write(r.content)
    log(filename + "\tOK\n")
    return 0

if __name__ == "__main__":
    get_json(href="https://cdn.jsdelivr.net/gh/Rcrwrate/Stellaris/main.json")