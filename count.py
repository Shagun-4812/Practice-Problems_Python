import threading

count=0
def counter():
    global count
    print(name," Started counting.....")
    for i in range(1000000):
        count += 1
        
        
    print(name," Finished counting.....")
    
Dinesh=threading.Thread(target=counter, args=("Dinesh"),)
Suresh=threading.Thread(target=counter, args=("Suresh"),)

Dinesh.start()
Suresh.start()

Dinesh.join()
Suresh.join()

print("Final count is ",count)