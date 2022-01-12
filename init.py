import StellarisAPI as API

if __name__ == "__main__":
    # API.welcome()
    http = API.HTTP(url_id=1)
    conf = API.CONF()
    main_json = http.get_json("main.json")
    # API.check.version(main_json)
    # basedir = API.check.dir()
    basedir = conf.load("Stellaris","basedir")[0]
    mod_list = API.check.list_mod(basedir)
    # mod_end = API.analysis.default(main_json,mod_list)
    # mod_force = API.analysis.force(main_json,mod_list)
    # conf.add("MOD","all",mod_list)
    # conf.add("MOD","all",mod_list)
    # conf.save()
    print(mod_list)
    # API.log(http)
