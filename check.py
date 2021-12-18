
from get import change_url_base,get_json
from msg import msg

def check_ver():
    change_url_base()
    json = get_json(href="main.json")
    if json != False:
        ver = json["ver"]
        if ver == msg("version"):
            print("您已经更新到最新版本")
        else:
            print("最新版本为：{}".format(ver))
            print("下载地址：{}".format(json["url"]))
    else:
        print("检查更新失败，请稍后重试")




if __name__ == "__main__":
    check_ver()