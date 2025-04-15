import threading


global_sum = 0

lock = threading.Lock()

def sum_array(arr):
    global global_sum
    local_sum = sum(arr)
    with lock:
        global_sum += local_sum

if __name__ == "__main__":
    # Four arrays
    arrays = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    # Create threads
    threads = []
    for arr in arrays:
        thread = threading.Thread(target=sum_array, args=(arr,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print(f"The total sum of all arrays is: {global_sum}")