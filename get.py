import requests,json,os,time
from msg import log
from conf import conf_set,conf_load

def change_url_base(url_id=""):
    if url_id == "":
        temp = conf_load("setting","url_base")
        if temp != False:
            url_id = temp
        else:
            url_id = 2

    global url
    if url_id == 0:
        url = "https://raw.githubusercontent.com/Rcrwrate/Stellaris/main/"
    elif url_id == 1:
        url = "https://cdn.jsdelivr.net/gh/Rcrwrate/Stellaris@latest/"
    else:
        url = "https://dl.phantom-sea-limited.ltd/Rcrwrate/Stellaris/main/"
    # log("change_url_base = "+url)
    conf_set("setting","url_base",str(url_id))
    return url


def get_json(name):
    try:
        href = url + "api/" + name + "?TID=" +str(time.time())
        # href = url + "api" + href
        session = requests.Session()
        session.trust_env = False
        r = session.get(href)
        r = json.loads(r.text)
        log("[href]:\t" + href + "\n" + str(name) + ": \n"+str(r))
        return r
    except Exception as err:
        log("[ERROR]:\thref: " + href + "\n" + str(err))
        print("或许是网络异常")
        return False


def download_file(filename,dltype="fix"):
    try:
        href = url + dltype + "/" + filename + "?TID=" +str(time.time())
        # href = url + dltype + "/" + filename
        session = requests.Session()
        session.trust_env = False
        r = session.get(href)
        path = '.log/' + dltype
        if not os.path.exists(path):
            os.makedirs(path)
        filename = ".log/" + dltype + "/" + filename
        with open(filename, 'wb') as fn:
            fn.write(r.content)
        log("[href]:\t" + href + "\t OK \n" )
        return 0
    except Exception as err:
        log("[ERROR]:\thref: " + href + "\n" + str(err))
        print("或许是网络异常")
        return False



if __name__ == "__main__":
    change_url_base(1)
    json = get_json("mod.json")
    if json != False:
        for k in json:
            print(json[k]["key"])
            download_file(json[k]["name"])