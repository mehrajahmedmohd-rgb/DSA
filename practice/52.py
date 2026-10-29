def soerted_array(arr):
    if len(arr)==1:
        return True

    if len(arr)==0:
        return True

    if arr[0]<arr[1]:
        return soerted_array(arr[1:])

    return False

arr = [1,2,7,4]
print(soerted_array(arr))