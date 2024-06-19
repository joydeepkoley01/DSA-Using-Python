# Creation of nodes
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start):
        self.start=start
    def isEmpty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.isEmpty():
            self.start=n
        else:
            temp=self.start
            while(temp.next is not None):
                temp=temp.next
            temp.next=n
            n.next=None