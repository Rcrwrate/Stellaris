from msg import conf_set

def analysis(json,mod_list):
    for k in json["mod_list"]:
        if k in mod_list:
            conf_set("Stellaris",json["mod_list"][k],"True")
            print("[TIPS]: {}已安装".format(json["mod_list"][k]))
        else:
            conf_set("Stellaris",json["mod_list"][k],"False")
            print("[TIPS]: {}未安装".format(json["mod_list"][k]))
    analysis_force(json,mod_list)

def analysis_force(json,mod_list):
    auto_fix = []
    for k in json["force_fix_list"]:
        if str(json["force_fix_list"][k][0]) in mod_list:
            if str(json["force_fix_list"][k][1]) in mod_list:
                auto_fix.append(k)
    if auto_fix != []:
        return auto_fix
    else:
        return None