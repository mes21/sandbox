import multiprocessing as mp
from time import sleep


class A(object):
    def __init__(self, *args, **kwargs):
        # do other stuff
        pass

    def do_something(self, i):
        sleep(0.2)
        print("int:", i)

    def run(self):
        processes = []

        for i in ["a", "b", "c"]:
            p = mp.Process(target=self.do_something, args=(i,))
            processes.append(p)

        [x.start() for x in processes]


if __name__ == "__main__":
    a = A()
    a.run()
