def large_ele(arr,n):
    largest=arr[0]
    for i in range(1,n):
        if arr[i]>largest:
            largest=arr[i]
            print(largest)
    return arr
arr=[3,2,1,5,4]
n=len(arr)
res=large_ele(arr,n)