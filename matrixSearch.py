def matrixSearch(arr,key,m,n):
    start=0
    end = (m*n)-1
    while(start<=end):
        mid = (start+end)/2
        r=mid/n
        c=mid%n
        if arr[r][c]==key:
            return "Found"
        elif arr[r][c] < key:
            start=mid+1
        else:
            end=mid-1
    return "Not Found"

A=[[1,3,5],
   [7,9,11],
   [13,15,17]]

print matrixSearch(A,4,3,3)
