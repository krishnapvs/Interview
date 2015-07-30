def smallCommonThreeArrays(A,B,C):
    ''' Find smallest common number in three sorted arrays '''
    for i in A:
        if i in B and i in C:
            return i
    return "No common element"

def smallestusinghash(A,B,C):
    # len function in python is O(1)
    hashtable={}
    for i in A:
        hashtable[i] = 1
                
    for i in B:
        if i in hashtable.keys():
            hashtable[i] += 1

    for i in C:
        if i in hashtable.keys():
            if hashtable[i] == 2:
                return i
    return "Not Found"
           

def binSearch(A,key,start,end):
    if end < start:
        return -1
    else:
        mid = start + (end - start)/2
        if A[mid]==key:
            return mid
        elif A[mid] > key:
            return binSearch(A,key,start,mid-1)
        else:
            return binSearch(A,key,mid+1,end)
            
    
def smallusingbinsearch(A,B,C):
    for i in A:
        if binSearch(B,i,0,len(B))!= -1 and binSearch(C,i,0,len(C))!= -1:
            return i
    return 'Not Found'



A = [1,3,5,6,7,8,9,10]
B = [-30,1,2,2,3,4,5,6,7,8987]
C = [2,3,4,64,645,67,54]
print smallCommonThreeArrays(A,B,C)
print smallestusinghash(A,B,C)
print smallusingbinsearch(A,B,C)
