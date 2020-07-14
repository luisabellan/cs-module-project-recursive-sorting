# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    k = 0

    # Traverse both array
    while i < len(arrA) and j < len(arrB):

        # Check if current element
        # of first array is smaller
        # than current element of
        # second array. If yes,
        # store first array element
        # and increment first array
        # index. Otherwise do same
        # with second array
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k = k + 1
            i = i + 1
        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1

    # Store remaining elements
    # of first array
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k = k + 1
        i = i + 1

    # Store remaining elements
    # of second array
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k = k + 1
        j = j + 1
    print("Array after merging")
    for i in range(len(arrA) + len(arrB)):
        print(str(merged_arr[i]), end=" ")

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr)//2  # middle element position
        left = arr[:mid]  # LHS
        right = arr[mid:]  # RHS

        merge_sort(left)  # Sorts LHS
        merge_sort(right)  # Sorts RHS

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    #print(arr)
    return arr


def printList(arr):
    print(arr)


# test code

arr = [12, 11, 13, 5, 6, 7]
print(f"Array before sorting: {arr}")
merge_sort(arr)
print(f"Sorted array: {arr}")


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input

''' 
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
 '''
