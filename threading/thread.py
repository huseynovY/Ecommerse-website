import time
import threading


def do_something():
    print("Process Started")
    time.sleep(1)
    print("Process End")
t1 = time.time()

threads = []

for i in range(20):
    th1 = threading.Thread(target=do_something)
    th1.start()
    threads.append(th1)

for element in threads:
    element.join()

t2 = time.time()

print(t2 - t1)