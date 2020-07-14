# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # Check base case
    if end >= start:

        mid = (end + start) // 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, target, mid + 1, end)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
target = 10

# Function call
result = binary_search(arr, target, 0, len(arr)-1)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
