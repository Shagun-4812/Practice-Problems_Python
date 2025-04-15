import threading

fork =threading.Lock()
knife =threading.Lock()
food = 100

def eat(name, left, right):
    global food
    
    while food >0:
        left.acquire()
        right.acquire()
        
        if food >0:
            food -=1
            print(name, "ate food. Remaining food", food)
            
        left.release()
        right.release()
        
threading.Thread(target=eat, args=("Philosopher 1", fork, knife)).start()
threading.Thread(target=eat, args=("Philosopher 2", knife, fork)).start()