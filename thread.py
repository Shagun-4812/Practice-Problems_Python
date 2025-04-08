import threading
import time 
def func1():
    for i in range(10):
        print("anything")
        
def func2():
    for i in range(10):
        print("something")

t1= threading.Thread(target=func1, args=[])
t2= threading.Thread(target=func2, args=[])       
        
func1()
func2()