import StellarisAPI as API
import os
if __name__ == "__main__":
    http = API.HTTP(url_id=1)
    main_json = http.get_json("main.json")
    # log(http)
    API.check.version(main_json)
    print(API.check.dir())

# C:\SteamLibrary\steamapps\workshop\content\281990\

    # dir = "C:\SteamLibrary\steamapps\common\Stellaris"
    # dir_out = dir.split("SteamLibrary")[0] + "SteamLibrary\steamapps\workshop\content\\281990\\"
    # print(dir_out)
    path = "C:\SteamLibrary\steamapps\common\Stellaris"

                

    print(final_dir)