import threading
import time

count = 0
lock = threading.Lock()  # Lock for thread safety

def thread_function(num_list):
    global count
    with lock:  # Ensuring only one thread modifies count at a time
        for i in num_list:
            count += i

# Creating and starting threads properly
t1 = threading.Thread(target=thread_function, args=([1, 2, 3, 4],))
t2 = threading.Thread(target=thread_function, args=([5, 6, 7, 8],))
t3 = threading.Thread(target=thread_function, args=([9, 10, 11, 12],))
t4 = threading.Thread(target=thread_function, args=([13, 14, 15, 16],))

t1.start()
t2.start()
t3.start()
t4.start()

# Waiting for threads to finish
t3.join()
print("Thread 3 finished")
t2.join()
print("Thread 2 finished")
t1.join()
print("Thread 1 finished")
t4.join()
print("Thread 4 finished")

time.sleep(1)
print(count)