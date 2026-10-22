
def dup(arr,n):
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=temp
arr=[1,1,2,2,2,3,3]
res=dup(arr,len(arr))
print(arr)