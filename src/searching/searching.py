# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # base case
    if end >= start:

        mid = (end + start) // 2

        # At the middle
        if arr[mid] == target:
            return mid

        # LHS
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)

        # RHS
        else:
            return binary_search(arr, target, mid + 1, end)

    else:
        # Element not found
        return False


# Test code
arr = [14, 32, 3, 0, 17]
target = 99

result = binary_search(arr, target, 0, len(arr)-1)

if result != False:
    print("Target at index", str(result))
else:
    print("Target not found")


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
