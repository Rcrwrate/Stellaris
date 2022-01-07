from StellarisAPI.HTTP.get import HTTP
from StellarisAPI.CONF.check import check
from StellarisAPI.log import log

if __name__ == "__main__":
    http = HTTP(url_id=1)
    main_json = http.get_json("main.json")
    # log(http)
    check.version(main_json)
    print(check.dir())
