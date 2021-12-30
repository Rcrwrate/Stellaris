import os
import time
import configparser


class CONF():
    def __init__(self):
        global PATH
        PATH = ".log/.ini"
        self.LOG = ""
        if not os.path.exists(".log"):
            os.makedirs(".log/")
        self.CONF = configparser.ConfigParser()
        try:
            self.CONF.read(PATH, encoding="utf-8")
        except Exception as err:
            self.log(err)
            print("[ERROR!]: .ini文件结构异常! 即将重新进行初始化")
            self.save()

    def add(self, sec, key, item):
        try:
            self.CONF.set(sec, key, item)
        except configparser.NoSectionError as err:
            self.CONF.add_section(err.section)
            self.CONF.set(sec, key, item)

    def remove(self, sec, key):
        try:
            self.CONF.remove_option(sec, key)
        except configparser.NoSectionError as err:
            # print("键值缺失!")
            self.log("[ERROR]:\t" + str(err))
            return False

    def load(self, sec, key):
        try:
            return self.CONF.get(sec, key)
        except configparser.NoSectionError as err:
            # print("键值缺失!")
            self.log("[ERROR]:\t" + str(err))
            return False
        except configparser.NoOptionError as err:
            # print("键值缺失!")
            self.log("[ERROR]:\t" + str(err))
            return False

    def save(self):
        self.CONF.write(open(PATH, "w+", encoding="utf-8"))

    def log(self, key):
        i = time.asctime(time.localtime(time.time()))
        key = '='*16 + i + '='*16 + '\n' + str(key)+'\n\n'
        self.LOG = self.LOG + key


if __name__ == "__main__":
    conf = CONF()
    conf.add("Stellaris", "test", "0")
    conf.remove("S", "0")
    print(conf.LOG)
    conf.save()
