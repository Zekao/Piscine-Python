from time import time


def progress(lst):
    start_time = time.time()
    for i in range(len(lst)):
        
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('=' * int(20 * i / len(lst)), 1 * i / len(lst) * 100))
        sys.stdout.write(" [%d/%d]" % (i, len(lst)))
        sys.stdout.write(" elapsed time %d seconds" % (time.time() - start_time))
        sys.stdout.flush()
        yield i
    i += 1
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('=' * int(20 * i / len(lst)), 1 * i / len(lst) * 100))
    sys.stdout.write(" elapsed time %d seconds" % (time.time() - start_time))
    sys.stdout.write(" [%d/%d]" % (i, len(lst)))
