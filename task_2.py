import numpy as np


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
 
    while low <= high:
        iterations += 1
        mid = (high + low) // 2
 
        # if x is greater than the value in the middle of the list, ignore the left half
        if arr[mid] < x:
            low = mid + 1
 
        # if x is less than the value in the middle of the list, ignore the right half
        elif arr[mid] > x:
            high = mid - 1
 
        # otherwise x is present at the position
        else:
            upper_bound = None
            if len(arr) > mid + 1:
                upper_bound = arr[mid + 1]

            return (iterations, upper_bound)
 
    # if the element is not found
    return -1


array_size = 100
arr = sorted(np.random.uniform(0,1000,(array_size,)))

# random index from arr array
random_index = np.random.randint(0, array_size - 1)
x = arr[random_index]

# if we want to check that element not in the array will return -1
# x = 4

result = binary_search(arr, x)
if result != -1:
    print(f'Element found in {result[0]} iterations. Upper bound element: {result[1]}')
else:
    print('Element is not present in array')
