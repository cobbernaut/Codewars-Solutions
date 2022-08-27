def find_uniq(arr):
    arr.sort()
    return(arr[-1] if arr[0] == arr[1] else arr[0])

##Alternative solution without list comprehension.
def find_uniq(arr):
    arr.sort()
    if arr[0]==arr[1]:
        return arr[-1]
    else:
        return arr[0]
   