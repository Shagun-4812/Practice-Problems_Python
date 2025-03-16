def merge_sort(arr):
    # Merge Sort
    # Best Time Complexity: O(n log n) - Example: [1, 2, 3, 4, 5]
    # Worst Time Complexity: O(n log n) - Example: [5, 4, 3, 2, 1]
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    print("Enter the elements of the array: ")
    arr = []
    for i in range(5):
        element = int(input())
        arr.append(element)
    result = merge_sort(arr)
    print("The sorted array is: ", result)

if __name__ == "__main__":
    main()