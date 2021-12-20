import os,time,configparser

global main_msg
main_msg = {
    "version":0.1,
    "debug":1
}


def msg(key):
    return main_msg[key]
    
def log(thing):
    # if conf_load("setting","debug") =="1":
    if msg("debug") == 1:
        i = time.asctime( time.localtime(time.time()) )
        path = '.log'
        if not os.path.exists(path):
            os.makedirs(path)
        with open('.log\log.log', 'a') as fn:
            fn.write('='*16+ i + '='*16 +'\n')
            fn.write(str(thing)+"\n\n")

# conf
def conf_init():
    conf_set("setting","debug","0")


def conf_set(sec,key,item):
    path = ".log/.ini"
    if not os.path.exists(".log"):
        os.makedirs(".log/")
    conf = configparser.ConfigParser()
    try:
        conf.read(path, encoding="utf-8")
    except Exception as err:
        print("[ERROR!]: .ini文件结构异常! 即将重新进行初始化")
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
        # print("键值缺失!")
        log("[ERROR]:\t" + str(err))
        return False
    except configparser.NoOptionError as err:
        # print("键值缺失!")
        log("[ERROR]:\t" + str(err))
        return False
    except Exception as err:
        log("[ERROR]:\t" + str(err))
        print("[ERROR!]: .ini文件结构异常! 即将重新进行初始化")
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
        # print("键值缺失!")
        log("[ERROR]:\t" + str(err))
        return False
    except Exception as err:
        log("[ERROR]:\t" + str(err))
        print("[ERROR!]: .ini文件结构异常! 即将重新进行初始化")
        conf.write(open(path, "w+", encoding="utf-8"))
        return False



if __name__ == "__main__":
    conf_init()
    print(conf_load("Stellaris","战舰少女r"))