from time import sleep
from my_minipack.progress import progress
from my_minipack.logger import logger


@logger
def test():
    list = range(800)
    ret = 0
    for elem in progress(list):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)


test()
