import os
def test():
    with open("fix/WG_lady_ship_sizes.txt",encoding='utf-8') as f:
        fn = f.readlines()
        l = fn[0].split(" ")
        print(l[2] == "0.1\n")
        print(float(l[2]))
        fn[0] = "# fixed 0.0\n"


    with open("fix/WG_lady_ship_sizes2.txt","w",encoding='utf-8') as f:
        for line in fn:
            f.write(line)

def test2():
    global a
    a = 1

def test3():
    print(a)

if __name__ == "__main__":
    # dir = input()
    # list_dir = os.listdir(basedir)
    # print(list_dir)
    test()