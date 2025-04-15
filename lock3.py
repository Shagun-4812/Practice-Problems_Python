import threading
import time
import random

lock = threading.Lock()

def first_person(l):
    print("Person one occupies the room")
    time.sleep(1)  
    print("Person one leaves the room")
    l.release()  
    
def second_person(l):
    l.acquire()  
    print("Person two occupies the room")
    time.sleep(1) 
    print("Person two leaves the room")
    l.release()  
    
t1 = threading.Thread(target=first_person, args=(lock,))
t2 = threading.Thread(target=second_person, args=(lock,))

t1.start()
t2.start()  

# in case of join until all the joint threads completee the main thread wont execute