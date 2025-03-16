def quick_sort(arr):
    # Quick Sort
    # Best Time Complexity: O(n log n) - Example: [1, 2, 3, 4, 5]
    # Worst Time Complexity: O(n^2) - Example: [5, 4, 3, 2, 1]
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def main():
    print("Enter the elements of the array: ")
    arr = []
    for i in range(5):
        element = int(input())
        arr.append(element)
    result = quick_sort(arr)
    print("The sorted array is: ", result)

if __name__ == "__main__":
    main()