import os,json,re,sys
from msg import *
from check import *
from get import *
from anslysis import analysis

def init():
    print("[SYSTEM]: 初始化完成")
    conf_init()
    dir_conf_save()

def main():
    if not os.path.exists(".log"):
        init()
    change_url_base()
    main = get_json("main.json")
    check_ver(main)

    inputs = re.split('\\s+', get('>').strip())
    while True:
        if inputs[0].startswith('q'):
            sys.exit()
        elif inputs[0].startswith('i'):
            init()
        elif inputs[0].startswith('a'):
            analysis(main,conf_load("Stellaris","mods"))
        # elif inputs[0].startswith('r'):
        # elif inputs[0].startswith('i'):
        elif inputs[0].startswith('u'):
            main = get_json("main.json")
            check_ver(main)
        elif inputs[0].startswith('v'):
            print("[SYSTEM]: 当前版本为{}".format(main["ver"]))
        inputs = re.split('\\s+', get('>').strip())

def get(prompt, default=None):
    while True:
        ret = input(prompt)
        if ret != '':
            return ret
        elif default is not None:
            return default

if __name__ == "__main__":
    main()