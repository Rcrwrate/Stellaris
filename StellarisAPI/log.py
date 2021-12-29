import os


def log(CLASS):
    try:
        thing = CLASS.LOG
    except Exception as err:
        print(err)
    path = '.log'
    if not os.path.exists(path):
        os.makedirs(path)
    with open('.log\log.log', 'a') as fn:
        fn.write(str(thing))
