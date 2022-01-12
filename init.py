import StellarisAPI as API

if __name__ == "__main__":
    # API.welcome()
    http = API.HTTP(url_id=1)
    main_json = http.get_json("main.json")
    API.check.version(main_json)
    print(API.check.dir())
    # API.log(http)
