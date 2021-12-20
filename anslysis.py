from msg import conf_set
from replace import check_and_replace
from get import download_file

def analysis(json,mod_list,mod):
    for k in json["mod_list"]:
        if k in mod_list:
            conf_set("Stellaris",json["mod_list"][k],"True")
            print("[TIPS]: {}已安装".format(json["mod_list"][k]))
        else:
            conf_set("Stellaris",json["mod_list"][k],"False")
            print("[TIPS]: {}未安装".format(json["mod_list"][k]))
    analysis_force(json,mod_list,mod)

def analysis_force(json,mod_list,mod):
    auto_fix = []
    for k in json["force_fix_list"]:
        if str(json["force_fix_list"][k][0]) in mod_list:
            if str(json["force_fix_list"][k][1]) in mod_list:
                auto_fix.append(k)
    if auto_fix != []:
        print("[INF]: 已检测到冲突，正在进行强制修复")
        for i in auto_fix:
            download_file(mod[i]["name"])
            check_and_replace(mod[i])
        print("[INF]: 修复完成")
    else:
        return None