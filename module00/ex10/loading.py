import sys, time

def ft_progress(lst):
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


def main():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)

if __name__=="__main__":
    main()