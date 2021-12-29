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
        key = '='*16 + i + '='*16 + '\n' + str(key)+'\n'
        self.LOG = self.LOG + key


if __name__ == "__main__":
    http = HTTP(url_id=1)
    print(http.LOG)
