from HTTP.get import HTTP
from log import log

if __name__ == "__main__":
    http = HTTP(url_id=1)
    http.get_json("main.json")
    log(http)
