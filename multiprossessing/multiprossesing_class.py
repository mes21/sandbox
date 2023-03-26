import keyboard  # using module keyboard
from multiprocessing import Process, freeze_support, set_start_method, Lock
import time
import asyncio

# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed("q"):  # if key 'q' is pressed
#             print("You Pressed A Key!")
#             break  # finishing the loop
#     except:
#         break  # if user pressed a key other than the given key the loop will break


# def worker(key):
#     print("start worker:", key)


class MultiP(object):
    def __init__(self, processes) -> None:

        self.processes = processes
        self.processList = []

    def worker(self, key):
        print("start self worker:", key)

    def run(self):

        for p in self.processes:
            px = Process(target=self.worker, args=(f"w{p}",))
            self.processList.append(px)
        [p.start() for p in self.processList]

    def stop(self):
        [p.join() for p in self.processList]


def main():

    workerList = ["A", "B", "C"]

    mp = MultiP(workerList)
    mp.run()

    time.sleep(1)

    mp.stop()


if __name__ == "__main__":
    main()
