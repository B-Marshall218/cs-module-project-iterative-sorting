def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Pick the middle and divide the number in half
        middle = (low + high) // 2
        guess = arr[middle]
        # If the guess is the target item then return it
        if arr[middle] == target:
            return middle
            # If the item doesnt = target and is larger than
        if guess > target:
            high = middle - 1
            # If its less than:
        else:
            low = middle + 1

    return -1  # not found
