def array_sorted(arr):
    if len(arr)==1:
        return True

    if len(arr)==0:
        return True

    if arr[0] > arr[1]:
        return False 

    return array_sorted(arr[1:])

arr=[2,4,3,2]

print(array_sorted(arr))