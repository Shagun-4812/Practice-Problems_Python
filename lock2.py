import threading
import time
def first_person():
    print("person one occupies the room")
    time.sleep(1)
    print("person one leaves the room")
    
    
def second_person():
    print("person two occupies the room")
    time.sleep(1)
    print("person two leaves the room")
    
    
t1= threading.Thread(target=first_person)
t2= threading.Thread(target=second_person)
t1.start()
t2.start()