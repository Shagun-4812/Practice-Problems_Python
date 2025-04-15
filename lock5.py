import threading

import time

sem= threading.Semaphore(2)

def worker(name):
    print(f"{name} is waiting to acquire the semaphore")
    with sem:
        print(f"{name} has acquired the semaphore")
        time.sleep(2)  
        print(f"{name} is releasing the semaphore")
for i in range(5):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    t.start()
    
# in multiprcessing theadinf we exedcute simultanieor in threading smname memory space where as in mutlti differnt space so in input output case iuts fine but in case its cimputattional problems u r advised to use multiprocess
