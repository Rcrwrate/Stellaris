import configparser,os
from msg import log

def conf_set(sec,key,item):
    path = ".log/.ini"
    if not os.path.exists(".log"):
        os.makedirs(".log/")
    conf = configparser.ConfigParser()
    try:
        conf.read(path, encoding="utf-8")
    except Exception as err:
        print(".ini文件结构异常! 即将重新进行初始化")
    try:
        conf.set(sec ,key ,item)
    except configparser.NoSectionError as err:
        conf.add_section(err.section)
        conf.set(sec ,key ,item)
    conf.write(open(path, "w+", encoding="utf-8"))


def conf_load(sec,key):
    path = ".log/.ini"
    if not os.path.exists(".log/"):
        os.makedirs(".log/")
    conf = configparser.ConfigParser()
    conf.read(path, encoding="utf-8")
    try:
        return conf.get(sec,key)
    except configparser.NoSectionError as err:
        print("键值缺失!")
        log("[ERROR]:\t" + str(err))
        return False
    except configparser.NoOptionError as err:
        print("键值缺失!")
        log("[ERROR]:\t" + str(err))
        return False
    except Exception as err:
        log("[ERROR]:\t" + str(err))
        print(".ini文件结构异常! 即将重新进行初始化")
        conf.write(open(path, "w+", encoding="utf-8"))
        return False


def conf_remove_key(sec,key):
    path = ".log/.ini"
    if not os.path.exists(".log/"):
        os.makedirs(".log/")
    conf = configparser.ConfigParser()
    conf.read(path, encoding="utf-8")
    try:
        conf.remove_option(sec,key)
        conf.write(open(path, "w+", encoding="utf-8"))
    except configparser.NoSectionError as err:
        print("键值缺失!")
        log("[ERROR]:\t" + str(err))
        return False
    except Exception as err:
        log("[ERROR]:\t" + str(err))
        print(".ini文件结构异常! 即将重新进行初始化")
        conf.write(open(path, "w+", encoding="utf-8"))
        return False


if __name__ == "__main__":
    conf_remove_key("change","wg_lady_ship_sizes.txt")