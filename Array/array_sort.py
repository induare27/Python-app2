def sort(arr,n):
    for i in range(1,n):
        if arr[i]<=arr[i-1]:
            return False
    return True
arr=[1,2,2,3,4,5]
sort(arr,len(arr))