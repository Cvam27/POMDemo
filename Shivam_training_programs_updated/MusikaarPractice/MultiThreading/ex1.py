import time
from threading import *


class demo(Thread):
    def run(self):
        for i in range(100):
            print("hi")
            time.sleep(1)


class demo2(Thread):
    def run(self):
        for i in range(100):
            print("hello")
            time.sleep(1)


o = demo()
p = demo2()
o.start()
time.sleep(0.1)
p.start()
