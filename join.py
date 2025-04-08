import threading
import time
count = 0

def counter(name):
    global count

    print(name, "starting count")
    for i in range(1000000):
        count += 1

    print(name, "count STOPPED")

Dinesh = threading.Thread(target=counter, args=["Dinesh"])
Deepak = threading.Thread(target=counter, args=["Deepak"])

Dinesh.start()
Deepak.start()

Deepak.join()
Dinesh.join()

print("Final count is", count)
