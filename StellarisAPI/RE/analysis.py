class analysis():
    @staticmethod
    def default(main_json, mod_list):
        mods = {}
        for k in main_json["mod_list"]:
            if k in mod_list:
                mods[main_json["mod_list"][k]] = True
                print("[TIPS]: {}已安装".format(main_json["mod_list"][k]))
            else:
                mods[main_json["mod_list"][k]] = False
                print("[TIPS]: {}未安装".format(main_json["mod_list"][k]))
        return mods

    @staticmethod
    def force(main_json, mod_list):
        auto_fix = []
        for k in main_json["force_fix_list"]:
            if str(main_json["force_fix_list"][k][0]) in mod_list:
                if str(main_json["force_fix_list"][k][1]) in mod_list:
                    auto_fix.append(k)
        if auto_fix != []:
            print("[WARN]: 已检测到冲突，正在进行强制修复")
            return auto_fix
            # print("[INF]: 修复完成")
        else:
            return None
