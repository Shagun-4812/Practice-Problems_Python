import threading
import time
import random

lock = threading.Lock()

def first_person(l):
    l.acquire()  # Acquire the lock
    print("Person one occupies the room")
    time.sleep(1)  # Simulate time spent in the room
    print("Person one leaves the room")
    l.release()  # Release the lock
    
def second_person(l):
    l.acquire()  # Acquire the lock
    print("Person two occupies the room")
    time.sleep(1)  # Simulate time spent in the room
    print("Person two leaves the room")
    l.release()  # Release the lock
    
t1 = threading.Thread(target=first_person, args=(lock,))
t2 = threading.Thread(target=second_person, args=(lock,))

t1.start()
t2.start()  

# in case of join until all the joint threads completee the main thread wont execute