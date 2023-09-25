import threading
import time


def y():
    x = 2
    while True:
        time.sleep(.01)
        x *= 1.1
t = []
for x in range(100):
    _t = threading.Thread(target=y)
    t.append(_t)

print(len(t))
for i in t:
    i.start()