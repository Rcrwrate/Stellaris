from msg import conf_set

def analysis(json,mod_list):
    for k in json["mod_list"]:
        if k in mod_list:
            conf_set("Stellaris",json["mod_list"][k],"True")
        else:
            conf_set("Stellaris",json["mod_list"][k],"False")
    # if "1481972266" in mod_list:
    #     conf_set("Stellaris","ACOT","True")
    # else:
    #     conf_set("Stellaris","ACOT","False")
    # if "1747099270" in mod_list:
    #     conf_set("Stellaris","WGRAMS","True") #战舰少女R
    # else:
    #     conf_set("Stellaris","WGRAMS","False")