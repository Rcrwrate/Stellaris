from conf import conf_load,conf_set,conf_remove_key
from msg import log

def check_and_replace(json):
    name = ".log/fix/" + json["name"]
    path = conf_load("Stellaris","dir") + json["key"]
    ori = file_ver(path)
    fix = file_ver(name)
    if ori == 0.0:
        save_orinal_file(path,json)
        replace_file(path,json)
    elif fix == ori:
        return False
    else:
        replace_file(path,json)
        return True

def file_ver(path):
    with open(path,encoding='utf-8') as f:
        fn = f.readlines()
        try:
            return float(fn[0].split(" ")[2])
        except ValueError as err:
            return 0.0


def save_orinal_file(path,json):
    name = ".log/.cache/" + json["name"]
    if not os.path.exists('.log/.cache/'):
        os.makedirs('.log/.cache/')
    with open(path,encoding='utf-8') as f:
        fn = f.readlines()
        with open(name,"w",encoding='utf-8') as f2:
            for line in fn:
                f2.write(line)
    log("[FILE_SAVE]:\t" + json["name"] + "\tOK")
    conf_set("change",json["name"],path)

# 懒得合并，就这样吧
def replace_file(path,json):
    fix_path = ".log/fix/" + json["name"]
    with open(fix_path,encoding='utf-8') as f:
        fn = f.readlines()
        with open(path,"w",encoding='utf-8') as f2:
            for line in fn:
                f2.write(line)
    log("[FILE_REPLACED]:\t" + json["name"] + "\tOK")


def restore_file(name):
    path = conf_load("change",name)
    if path != False:
        ori_file = ".log/.cache/" + str(name)
        try:
            with open(ori_file,encoding='utf-8') as f:
                fn = f.readlines()
                with open(path,"w",encoding='utf-8') as f2:
                    for line in fn:
                        f2.write(line)
        except Exception as err:
            log("[ERROR]:\t" + str(err))
            print("恢复失败，请检查日志")
        else:
            log("[RESTORE]:\t" + str(name) + "\tOK")
            conf_remove_key("change",name)

if __name__ == "__main__":
    # from get import *
    # change_url_base(url_id = 1)
    # mod_list = get_json("mod.json")
    # for i in ["1"]:
    #     print(check_and_replace(mod_list[i])) 
    
    restore_file("WG_lady_ship_sizes.txt")