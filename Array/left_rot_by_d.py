
def left_rot(arr,n,d):
    d=d%n
    temp=[]
    for i in range(0,d):
        temp.append(arr[i])   #adding in temp
    for i in range(d,n):
        arr[i-d]=arr[i]      #shifting
    for i in range(n-d,n):
        arr[i]=temp[i-(n-d)] #shiting from temp to arr

arr=[1,2,3,4,5,6,7]
res=left_rot(arr,len(arr),3)
print(arr)
        
