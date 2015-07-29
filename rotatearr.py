def rotateArr(arr,n):
    # rotates array right to left for n positions and returns the rotated array
    return arr[-n:] + arr[:-n]



a=[9,2,1,4,64,3,532,2,5]
print a
print rotateArr(a,4)
