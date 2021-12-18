import requests

def download_file(href):
    session = requests.Session()
    session.trust_env = False
    r = session.get(href)
    print(r.text)
    return 0


if __name__ == "__main__":
    download_file(href="https://cdn.jsdelivr.net/gh/Rcrwrate/Stellaris")