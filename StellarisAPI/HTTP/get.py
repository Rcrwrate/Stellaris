import requests
import json
import os
import time


class HTTP():
    def __init__(self, url_id=2):
        self.UID = url_id
        self.LOG = ""
        self.URL = self.change_url_base(self.UID)

    def change_url_base(self, url_id):
        if url_id == 0:
            url = "https://raw.githubusercontent.com/Rcrwrate/Stellaris/main/"
        elif url_id == 1:
            url = "https://cdn.jsdelivr.net/gh/Rcrwrate/Stellaris@latest/"
        else:
            url = "https://dl.phantom-sea-limited.ltd/Rcrwrate/Stellaris/main/"
        self.log("change_url_base = {}".format(url))
        # conf_set("setting","url_base",str(url_id))
        return url

    def log(self, key):
        i = time.asctime(time.localtime(time.time()))
        key = '='*16 + i + '='*16 + '\n' + str(key)+'\n\n'
        self.LOG = self.LOG + key

    def get_json(self, name):
        try:
            # href = self.URL + "api/" + name + "?TID=" + str(time.time())
            href = self.URL + "api/" + name
            session = requests.Session()
            session.trust_env = False
            session.keep_alive = False
            r = session.get(href)
            r = json.loads(r.text)
            self.log("[href]:\t" + href + "\n" + str(name) + ": \n"+str(r))
            return r
        except Exception as err:
            self.log("[ERROR]:\thref: " + href + "\n" + str(err))
            print("[ERROR]:\t或许是网络异常")
            return False

    def download_file(self,filename, dltype="fix"):
        try:
            # href = self.URL + dltype + "/" + filename + "?TID=" + str(time.time())
            href = self.URL + dltype + "/" + filename
            session = requests.Session()
            session.trust_env = False
            session.keep_alive = False
            r = session.get(href)
            path = '.log/' + dltype
            if not os.path.exists(path):
                os.makedirs(path)
            filename = ".log/" + dltype + "/" + filename
            with open(filename, 'wb') as fn:
                fn.write(r.content)
            self.log("[href]:\t" + href + "\t OK \n")
            return 0
        except Exception as err:
            self.log("[ERROR]:\thref: " + href + "\n" + str(err))
            print("[ERROR]:\t或许是网络异常")
            return False


if __name__ == "__main__":
    http = HTTP(url_id=1)
    http.get_json("main.json")
    # http.get_json("mod.json")
    http.download_file("WG_lady_ship_sizes.txt")
    print(http.LOG)
