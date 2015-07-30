'''There is a stair with n levels. A frog can jump up one level or two levels at one time on the
stair. How many ways are there for the frog to jump from the bottom of the stairs to the top?
For example, there are three choices for the frog to jump up a stair with three levels: (1) it jumps in three steps,
one level for each jump; (2) it jumps in two steps, one level for the first jump and two levels for the second jump;
or (3) it jumps with two steps, two levels for the first step and one level for the last jump.'''

def frogSteps(n,table=[]):
    if table==[]:
        table=[None] * (n+1)
        table[0:3]=[0,1,2]
    if  table[n] != None:
        return table[n]
    else:
        table[n]=(frogSteps(n-2,table) + frogSteps(n-1,table))
        return table[n]


print frogSteps(10)

def fib(n):
    if n==1:
        return 2
    elif n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print fib(9)
