class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class BinTree:
    root=None
    def add(self,key):
        if self.root == None:
            self.root=Node(key)
        else:
            if self.root.key>=key:
                temp=self.root.left
                self.root.left=Node(key)
                if temp:
                    if key >= temp.key:
                        self.root.left.left=temp
                    else:
                        self.root.left.right=temp
            else:
                temp=self.root.right
                self.root.right=Node(key)
                if temp:
                    if key >= temp.key:
                        self.root.right.left=temp
                    else:
                        self.root.right.right=temp

def inorder(tree):
    if not tree:
        return
    else:
        inorder(tree.left)
        print tree.key
        inorder(tree.right)


def inorder_iter(root):
    s=[] # initializing the stack
    done=False
    current=root
    while not(done):
        if current:
            s.append(current)
            current=current.left
        else:
            if len(s)==0:
                done=True
            else:
                current=s.pop()
                print current.key
                current=current.right


a=BinTree()

for i in range(10,0,-1):
    a.add(i)

#for i in range(6,11):
#    a.add(i)
inorder(a.root)
print "This is iterative"
inorder_iter(a.root)
