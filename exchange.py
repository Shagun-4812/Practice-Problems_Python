def exchange(arr):
    n = len(arr)
    for i in range(n-1):
        max = i  # Reset max to the current index i
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                max = j
        arr[i], arr[max] = arr[max], arr[i]
    return arr

def main():
    print("Enter the elements of the array: ")
    arr = []
    for i in range(5):
        element = int(input())
        arr.append(element)
    result = exchange(arr)
    print("The sorted array is: ", result)

if __name__ == "__main__":
    main()