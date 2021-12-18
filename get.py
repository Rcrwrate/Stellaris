import requests,json,os,time
from msg import log

def change_url_base(url_id = 2):
    global url
    if url_id == 0:
        url = "https://raw.githubusercontent.com/Rcrwrate/Stellaris/main/"
    elif url_id == 1:
        url = "https://cdn.jsdelivr.net/gh/Rcrwrate/Stellaris@latest/"
    else:
        url = "https://dl.phantom-sea-limited.ltd/Rcrwrate/Stellaris/main/"
    # log("change_url_base = "+url)


def get_json(href):
    try:
        href = url + href + "?TID=" +str(time.time())
        # href = url + href
        session = requests.Session()
        session.trust_env = False
        r = session.get(href)
        r = json.loads(r.text)
        log("href: " + href + "\nmain.json: "+str(r))
        return r
    except Exception as err:
        log("href: " + href + "\n" + str(err))
        print("或许是网络异常")
        return False


def download_file(filename):
    try:
        href = url + "fix/" + filename + "?TID=" +str(time.time())
        # href = url + "fix/" + filename
        session = requests.Session()
        session.trust_env = False
        r = session.get(href)
        path = '.log/fix'
        if not os.path.exists(path):
            os.makedirs(path)
        filename = ".log/fix/" + filename
        with open(filename, 'wb') as fn:
            fn.write(r.content)
        log("href: " + href + "\t OK \n" )
        return 0
    except Exception as err:
        log("href: " + href + "\n" + str(err))
        print("或许是网络异常")
        return False



if __name__ == "__main__":
    change_url_base()
    json = get_json(href="main.json")
    if json != False:
        print(json["fix_list"])
        for k in json["fix_list"]:
            download_file(json["fix_list"][k]["name"])