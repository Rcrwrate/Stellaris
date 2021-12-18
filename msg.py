import os
import time

global version
version = 0.1

def msg(key):
    return version
    
def log(thing):
    i = time.asctime( time.localtime(time.time()) )
    path = '.log'
    if not os.path.exists(path):
        os.makedirs(path)
    with open('.log\log.log', 'a') as fn:
        fn.write('='*16+ i + '='*16 +'\n')
        fn.write(str(thing)+"\n\n")
        

if __name__ == "__main__":
    log("test")