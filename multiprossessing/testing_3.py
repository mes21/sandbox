import multiprocessing as mp
from time import sleep


class A(object):
    def __init__(self, *args, **kwargs):
        # do other stuff
        pass
        self.abc = ["a", "b", "c"]
        self.processes = []

    def do_something(self, i):
        sleep(0.2)
        print("int:", i, self.abc)

    def run(self):

        for i in self.abc:
            p = mp.Process(target=self.do_something, args=(i,))
            p.start()
            self.processes.append(p)

        # [x.start() for x in self.processes]


if __name__ == "__main__":
    a = A()
    a.run()
