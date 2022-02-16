import time
from random import randint
import os


def log(func):

    def inner1(*args, **kwargs):
        begin = time.time()

        ret = func(*args, **kwargs)

        exec_time = time.time() - begin
        if exec_time < 1:
            exec_time = "%.10f" % (exec_time * 1000) + ' ms'
        else:
            exec_time = "%.10f" % exec_time + ' s '
        user = os.environ["USER"]
        func_name = str.replace(func.__name__, '_', ' ')
        func_name += ' ' * (19 - len(func_name))
        line = f'({user})Running: {func_name}[ exec-time = {exec_time} ]\n'

        log_file = open("machine.log", "a")
        log_file.write(line)
        log_file.close()

        return ret
    return inner1
