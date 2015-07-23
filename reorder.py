'''There are N+1 parking spots, numbered from 0 to N.
There are N cars numbered from 1 to N parked in various parking spots with one left empty.
Reorder the cars so that car #1 is in spot #1, car #2 is in spot #2 and so on.
Spot #0 will remain empty. The only allowed operation is to take a car and move it to the free spot.'''


def reorder(arr):
    '''Takes in a list as parking lots with the cars in the positions'''
    n=len(arr)
    for i in range(n):
        if arr[i]==None:
            arr[i]=arr[0]
            arr[0]=None
            break
    #print arr
    i=1
    while( i < n ):
        if arr[i]!=i:
            arr[0]=arr[i]
            for j in range(i+1,n):
                if arr[j]==i:
                    arr[i]=i
                    arr[j]=arr[0]
                    arr[0]=None
                    break
        i=i+1
    return arr


a=[1,2,3,4,None]
print reorder(a)
