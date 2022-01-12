from StellarisAPI.msg import msg as main_msg
import os

class check():
    @staticmethod
    def version(json):
        if json != False:
            if json["used"] != "True":
                print("[ALERT]: ！警告：程序已被禁止使用！")
                input("[ALERT]: 按回车键退出")
                sys.exit(-1)
            if json["ver"] == main_msg["version"]:
                print("[SYSTEM]: 您已经更新到最新版本")
            elif json["min_ver"] >= main_msg["version"]:
                print("[FORCE_UPDATA]: 最新版本为：{}".format(json["ver"]))
                print("[FORCE_UPDATA]: 您的版本为：{}".format(main_msg["version"]))
                print("[FORCE_UPDATA]: 下载地址：{}".format(json["url"]))
                input("[FORCE_UPDATA]: 您已经低于版本最低要求，请务必更新，按回车键退出")
                sys.exit(-1)
            else:
                print("[TIPS]: 最新版本为：{}".format(json["ver"]))
                print("[TIPS]: 您的版本为：{}".format(main_msg["version"]))
                print("[TIPS]: 下载地址：{}".format(json["url"]))
        else:
            print("[ERROR]: 检查更新失败，请稍后重试")
    
    @staticmethod
    def dir():
        path = os.getcwd()
        if path.find("Stellaris") != -1:
            if path.find("SteamLibrary") != -1:
                final_dir = str(path.split("SteamLibrary")[0]) + "SteamLibrary\workshop\content\\281990\\"
                if os.path.exists(final_dir):
                    print("[SYSTEM]: 已自动识别到Steam群星安装目录，等待联网分析mod列表")
                    return final_dir
            elif path.find("Steam") != -1:
                final_dir = str(path.split("Steam")[0]) + "steamapps\workshop\content\\281990\\"
                if os.path.exists(final_dir):
                    print("[SYSTEM]: 已自动识别到Steam群星安装目录，等待联网分析mod列表")
                    return final_dir
        for drive in ['C','D','E','F']:
            path = drive + ":\Program Files (x86)\Steam\steamapps\common\Stellaris"
            if os.path.exists(path):
                final_dir = drive + ":\Program Files (x86)\Steam\steamapps\workshop\content\\281990\\"
                if os.path.exists(final_dir):
                    print("[SYSTEM]: 已自动识别到Steam群星安装目录，等待联网分析mod列表")
                    return final_dir
        for drive in ['C','D','E','F']:
            path = drive + ":\SteamLibrary\steamapps\common\Stellaris"
            if os.path.exists(path):
                final_dir = drive + ":\SteamLibrary\steamapps\workshop\content\\281990\\"
                if os.path.exists(final_dir):
                    print("[SYSTEM]: 已自动识别到Steam群星安装目录，等待联网分析mod列表")
                    return final_dir
        print("[SYSTEM]: 未能自动识别到您的Steam群星安装目录，请手动输入：\n\t(需要同时包含Steam和Stellaris这俩个关键词)\n\t(可以在Steam库中对群星右键 > 管理 > 浏览本地文件)")
        path = input()
        if path.find("SteamLibrary") != -1:
            final_dir = str(path.split("SteamLibrary")[0]) + "SteamLibrary\steamapps\workshop\content\\281990\\"
        else:
            final_dir = str(path.split("Steam")[0]) + "Steam\steamapps\workshop\content\\281990\\"
        if os.path.exists(final_dir):
            print("[SYSTEM]: 路径正确，等待联网分析mod列表")
            return final_dir
        else:
            print("[ERROR!]: 路径识别失败，请重新识别或寻求开发者帮助")
    
    @staticmethod
    def list_mod(basedir):
        list_dir = os.listdir(basedir)
        return list_dir
