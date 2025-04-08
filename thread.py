import threading
import time 
def func1():
    for i in range(10):
        print("anything")
        
def func2():
    for i in range(10):
        print("something")
        
        
func1()
func2()