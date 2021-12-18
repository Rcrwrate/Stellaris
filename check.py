
from get import change_url_base,get_json
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



if __name__ == "__main__":
    change_url_base(1)
    json = get_json(href="main.json")
    check_ver(json)