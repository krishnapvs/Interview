def radixSort(arr):
    
    divisor=10
    div=1
    while(True):
        new=[[],[],[],[],[],[],[],[],[],[]]
        for i in arr:
            mod = i % divisor
            mod = mod / div
            new[mod].append(i)
        divisor *= 10
        div *= 10
        

        if len(new[0]) == len(arr):
            return new[0]
        arr=[]
        
        for i in new:
            for j in i:
                arr.append(j)
        


arr=[10,12,324,2131,4,21,32,1,4,5,8]
print radixSort(arr)
