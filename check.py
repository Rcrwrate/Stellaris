import os
from msg import msg

def check_ver(json):
    if json != False:
        if json["used"] != "True":
            print("！警告：程序已被禁止使用！")
            input("按回车键退出")
            import sys
            sys.exit(-1)
        ver = json["ver"]
        if ver == msg("version"):
            print("您已经更新到最新版本")
        else:
            print("最新版本为：{}".format(ver))
            print("您的版本为：{}".format(msg("version")))
            print("下载地址：{}".format(json["url"]))
    else:
        print("检查更新失败，请稍后重试")


def check_dir():
    path = os.getcwd()
    if path.find("Stellaris") != -1:
        if path.find("Steam") != -1:
            final_dir = str(path.split("Steam")[0]) + "steamapps\workshop\content\\281990\\"
            if os.path.exists(final_dir):
                print("已自动识别到Steam群星安装目录，正在分析mod列表")
                return final_dir
    for drive in ['C','D','E','F']:
        path = drive + ":\Program Files (x86)\Steam\steamapps\common\Stellaris"
        print(path)
        if os.path.exists(path):
            final_dir = drive + ":\Program Files (x86)\Steam\steamapps\workshop\content\\281990\\"
            if os.path.exists(final_dir):
                print("已自动识别到Steam群星安装目录，正在分析mod列表")
                return final_dir
    print("系统未能自动识别到您的Steam群星安装目录，请手动输入：\n(需要同时包含Steam和Stellaris这俩个关键词)\n(可以在Steam库中对群星右键 > 管理 > 浏览本地文件)")
    path = input()
    final_dir = str(path.split("Steam")[0]) + "Steam\steamapps\workshop\content\\281990\\"
    if os.path.exists(final_dir):
        print("路径正确，正在分析mod列表")
        return final_dir
    else:
        print("路径识别失败，请重新识别或寻求开发者帮助")

#D:\Program Files (x86)\Steam\steamapps\workshop\content\281990

if __name__ == "__main__":
    # from get import change_url_base,get_json
    # change_url_base(1)
    # json = get_json(href="main.json")
    # check_ver(json)

    print(check_dir())