def sort(a,b,arr):
    i=j=k=0
    while(i<len(a) and j<len(b)):
            if(a[i]<=b[j]):
                arr[k]=a[i]
                i+=1

            else:
                arr[k]=b[j]
                j+=1

            k+=1

    while(i<len(a)):
            arr[k]=a[i]
            i+=1
            k+=1

    while(j<len(b)):
            arr[k]=b[j]
            j+=1
            k+=1        

def mergesort(arr):
    if len(arr)<=1:
        return 

    mid=len(arr)//2
    first=arr[:mid]
    last=arr[mid:]

    mergesort(last)
    mergesort(first)

    sort(first,last,arr)



if __name__=="__main__":
    arr=[]
    n=int(input("number of elements\n"))

    for i in range(0,n):
        j=int(input("array elements\n"))

        arr.append(j)



    mergesort(arr)    
    print(arr)