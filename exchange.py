def exchange(arr):
    # Exchange Selection Sort
    # Best Time Complexity: O(n^2) - Example: [1, 2, 3, 4, 5]
    # Worst Time Complexity: O(n^2) - Example: [5, 4, 3, 2, 1]
    n = len(arr)
    for i in range(n-1):
        max_idx = i  # Reset max_idx to the current index i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
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