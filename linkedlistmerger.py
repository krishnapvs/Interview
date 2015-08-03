class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

class LinkedList:
    head=None
    tail=None
    def append(self,key):
        if self.head:
            node=Node(key)
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=node
            self.tail=temp.next
        else:
            self.head=Node(key)

    def print_list(self):
        temp=self.head
        while temp:
            print temp.key,' -> ',
            temp=temp.next
        print None

def linkedlistmerger(a,b):
    #7.	Merges two sorted linked lists.
    if a.head==None and b.head==None:
        return None
    elif a.head==None:
        return b
    elif b.head==None:
        return a
    else:
        c=LinkedList()
        run_a,run_b=a.head,b.head
        while run_a and run_b:
            if run_a.key <= run_b.key:
                c.append(run_a.key)
                run_a=run_a.next
            else:
                c.append(run_b.key)
                run_b=run_b.next
        while run_a:
            c.append(run_a.key)
            run_a=run_a.next
        while run_b:
            c.append(run_b.key)
            run_b=run_b.next
        return c

n1=LinkedList()
n2=LinkedList()
for i in range(0,20,2):
    n1.append(i)
    n2.append(i-1)


n1.print_list()
n2.print_list()
n3=linkedlistmerger(n1,n2)
n3.print_list()
