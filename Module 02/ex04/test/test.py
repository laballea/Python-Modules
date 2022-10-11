from time import sleep
import my_minipack.logger
import my_minipack.progress

listy = range(3333)
ret = 0


@my_minipack.logger.log
def test():
    ret = 0
    for elem in my_minipack.progress.ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)


test()
