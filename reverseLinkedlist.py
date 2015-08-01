'''Reverse a singly linked list. '''

class Node:
    def __init__(self, key):
        self.cargo = key
        self.next = None

class linkedList:
    def __init__(self,cargo):
        self.head=Node(cargo)
        self.length=1

    def addList(self,cargo):
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=Node(cargo)
        self.length += 1

    def printList(self):
        temp=self.head
        while(temp):
            print temp.cargo
            temp=temp.next
        print "END"

def reverseLL(linked_list):
# reverses a linked list but needs optimization
    head=linked_list.head
    temp=head.next
    head.next=None
    while temp:
        inter=temp.next
        temp.next=head
        head=temp
        temp=inter
    linked_list.head=head
    
    
l1=linkedList(1)


for i in range(2,10):
    l1.addList(i)

l1.printList()

reverseLL(l1)

l1.printList()
        
    
