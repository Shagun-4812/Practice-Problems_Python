

def insertion_sort(arr):
    # Insertion Sort
    # Best Time Complexity: O(n) - Example: [1, 2, 3, 4, 5]
    # Worst Time Complexity: O(n^2) - Example: [5, 4, 3, 2, 1]
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    print("Enter the elements of the array: ")
    arr = []
    for i in range(5):
        element = int(input())
        arr.append(element)
    result = insertion_sort(arr)
    print("The sorted array is: ", result)

if __name__ == "__main__":
    main()