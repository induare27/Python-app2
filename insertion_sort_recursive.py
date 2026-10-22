def ins_sort(arr,n,i):
    if(i==n):
            return
    j=i
    while(j>0 and arr[j-1]>arr[j]):
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j=j-1
    ins_sort(arr,n,i+1)
        
arr=[13,46,24,52,20,9]
n=len(arr)
re=ins_sort(arr,n,0)
print(arr)