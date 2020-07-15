# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # base case
    if end >= start:
        # easiest way of finding middle element, but unsafe, as it could overflow in other
        # mid = (end + start) // 2
        '''Imagine that start is equal to the maximum range of an integer.
        Now, adding anything to start will result in an integer overflow.
        As we need to add both numbers first to evaluate our equation, an overflow might occur.'''

        ''' The safest way to find the middle of two numbers without getting an overflow is as follows,
         although we don't have that problem in Python, I'm using this way instead to avoid making this mistake when working with other languages.'''

        mid = start + (end-start) // 2

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
        # Element is not present in the array
        return -1


# Test code
arr = [14, 32, 3, 0, 17]
target = 3

result = binary_search(arr, target, 0, len(arr)-1)

if result != -1:
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
    start = 0
    end = len(arr) - 1
    is_ascending = arr[start] < arr[end]
    while start <= end:
        # calculate the middle of the current range
        mid = start + (end - start) // 2

        if target == arr[mid]:
            return mid

        if is_ascending:  # ascending order
            if target < arr[mid]:
                end = mid - 1
            # the 'target' can be in the first half

            else:  # target > arr[mid]
                start = mid + 1
                # the 'target' can be in the second half

        else:  # descending order
            if target > arr[mid]:
                end = mid - 1
                # the 'target' can be in the first half
            else:  # target < arr[mid]
                start = mid + 1
                # the 'target' can be in the second half

    # element not found
    return -1


# test code
print(agnostic_binary_search([4, 6, 10], 10))
print(agnostic_binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(agnostic_binary_search([10, 6, 4], 10))
print(agnostic_binary_search([10, 6, 4], 4))
