def bubble_sort(arr):
    # Bubble Sort
    # Best Time Complexity: O(n) - Example: [1, 2, 3, 4, 5]
    # Worst Time Complexity: O(n^2) - Example: [5, 4, 3, 2, 1]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    print("Enter the elements of the array: ")
    arr = []
    for i in range(5):
        element = int(input())
        arr.append(element)
    result = bubble_sort(arr)
    print("The sorted array is: ", result)

if __name__ == "__main__":
    main()