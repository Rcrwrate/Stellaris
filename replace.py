
def check_file_which_neet_replace_ver(path,name):
    name = ".log/fix/" + str(name)
    if file_ver(path) == file_ver(name):
        return True
    else:
        return False

def file_ver(path):
    with open(path,encoding='utf-8') as f:
        fn = f.readlines()
        try:
            return float(fn[0].split(" ")[2])
        except ValueError as err:
            return 0.0


if __name__ == "__main__":
    print(file_ver("fix/WG_lady_ship_sizes2.txt"))