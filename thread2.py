import threading

import random
import time

count=0

def thread_function(name, sleep_time):
    global count
    print(name, "started")
    
    time.sleep(sleep_time)
    print(name, "finished")
    
t3= threading.Thread(target=thread_function, args=("3", 3))
t3.start()
t2= threading.Thread(target=thread_function, args=("2", 2))
t2.start()
t1= threading.Thread(target=thread_function, args=("1", 1))
t1.start()

t3.join()
print("t3 ended")

t2.join()
print("t2 ended")   
t1.join()
print("t1 ended")