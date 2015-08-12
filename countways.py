''' A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or
3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.'''

def numOfWays(n,l=[]):
#    print l
    if n<0:
        return 0
    if not l:
        l=[1,1]
    if n < len(l):
        return l[n]
    else:
        l.append(numOfWays(n-1,l) + numOfWays(n-2,l) + numOfWays(n-3,l))
        return l[n]

def countWays(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return countWays(n-1) + countWays(n-2) + countWays(n-3)


#print numOfWays(30)
print countWays(30)
