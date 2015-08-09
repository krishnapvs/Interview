from random import Random
class BinTree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

    def addLeft(self,key):
        if self.left:
            temp=self.left
            self.left=BinTree(key)
            self.left.right=temp
        else:
            self.left=BinTree(key)

    def addRight(self,key):
        if self.right:
            temp=self.right
            self.right=BinTree(key)
            self.right.left=temp
        else:
            self.right=BinTree(key)

    def addNode(self,key):
        if self.key >= key:
            if self.left:
                self.left.addNode(key)
            else:
                self.left=BinTree(key)
        else:
            if self.right:
                self.right.addNode(key)
            else:
                self.right=BinTree(key)

def inorder(tree):
    if not tree:
        return
    else:
        inorder(tree.left)
        print tree.key
        inorder(tree.right)


def compareTree(a,b):
    if a==None and b==None:
        return True
    elif a==None or b==None:
        return False
    else:
        return compareTree(a.left,b.left) and compareTree(a.right,b.right)

rand=Random()

    
t1=BinTree(10)
for i in range(10):
    t1.addNode(rand.randint(0,100))
'''t2=BinTree(1)
for i in range(5):
    t2.addLeft(i)
    t2.addRight(i)
t2.addRight(8)
'''
inorder(t1)
#print compareTree(t1,t2)
