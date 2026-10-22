def large_ele(arr,n):
    largest=arr[0]
    for i in range(1,n):
        if arr[i]>largest:
            largest=arr[i]
            print(largest)
    slargest=-1
    for j in range(1,n):
        if arr[j]>slargest and arr[j]!=largest:
            slargest=arr[j]
    print(slargest)
    return arr
arr=[3,2,1,5,4]
n=len(arr)
res=large_ele(arr,n)
    