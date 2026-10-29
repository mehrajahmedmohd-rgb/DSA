def sorted_array(arr):
    if len(arr)==1:
        return True

    if len(arr)==0:
        return True       

    if arr[0] > arr[1]:
        return False


    return sorted_array(arr[1:]) 

arr=[1,2,9,5]
print(sorted_array(arr))
