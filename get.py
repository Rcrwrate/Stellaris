import requests
import json
from msg import log

def change_url_base(url_id = 2):
    global url
    if url_id == 0:
        url = "https://raw.githubusercontent.com/Rcrwrate/Stellaris/main/"
    elif url_id == "1":
        url = "https://cdn.jsdelivr.net/gh/Rcrwrate/Stellaris/"
    else:
        url = "https://dl.phantom-sea-limited.ltd/Rcrwrate/Stellaris/main/"
    log("change_url_base = "+url)


def get_json(href):
    href = url + href
    session = requests.Session()
    session.trust_env = False
    r = session.get(href)
    r = json.loads(r.text)
    log("main.json: "+str(r))
    return r


def download_file(filename, href):
    href = url + href
    session = requests.Session()
    session.trust_env = False
    r = session.get(href)
    path = '.log'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(filename, 'wb') as fn:
        fn.write(r.content)
    log(filename + "\tOK\n")
    return 0


if __name__ == "__main__":
    change_url_base()
    json = get_json(href="main.json")
    print(json["lady"]["key"])