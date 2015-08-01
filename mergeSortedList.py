class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

    def addNode(self,key):
        if self.next== None:
            self.next=Node(key)
        else:
            temp=self
            while temp.next:
                temp=temp.next
            temp.next=Node(key)
            
    def printList(self):
        temp=self
        while(temp):
            print temp.key
            temp=temp.next

def mergeList(l1,l2):
    ''' merges two sorted linked lists'''
    if l1.key<=l2.key:
        head=l1
        l1=l1.next
    else:
        head=l2
        l2=l2.next
    runner=head
    while l1 and l2:
        if l1.key <= l2.key:
            runner.next=l1
            l1=l1.next
        else:
            runner.next=l2
            l2=l2.next
        runner=runner.next
    while l1:
        runner.next=l1
        l1=l1.next
        runner=runner.next
    while l2:
        runner.next=l2
        l2=l2.next
        runner=runner.next
    return head

l1=Node(1)
l2=Node(1)

for i in range(0,20,2):
    l1.addNode(i)

for i in range(1,20,2):
    l2.addNode(i)
#l1.printList()
#l2.printList()
head=mergeList(l1,l2)
head.printList()
