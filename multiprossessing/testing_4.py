import multiprocessing as mp
from time import sleep


class A(object):
    def __init__(self, *args, **kwargs):
        # do other stuff
        pass
        self.abc = ["a", "b", "c"]

    def do_something(self, i):
        sleep(0.2)
        print("int:", i, self.abc)

    def run(self, plist):

        for i in self.abc:
            p = mp.Process(target=self.do_something, args=(i,))
            p.start()
            plist.append(p)

    def stop(self, plist):
        [p.join() for p in plist]


if __name__ == "__main__":

    pList = []
    a = A()
    a.run(pList)

    a.stop(pList)
