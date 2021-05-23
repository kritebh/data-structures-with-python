class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        i=self.head
        while i.next:
            i=i.next
        i.next=Node(data,None)
    
    def insert_lots_value(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        c=0
        i=self.head
        while i:
            c=c+1
            i=i.next
        return c

    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Index out of range")

        if index==0:
            self.insert_at_begining(data)
            return
        c=0
        i=self.head
        while i:
            if c==index-1:
                node=Node(data,i.next)
                i.next=node
                break
            i = i.next
            c=c+1
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Index out of range")

        if index==0:
            self.head=self.head.next
            return
        count=0
        i=self.head
        while i:
            if count==index-1:
                i.next = i.next.next
                break
            i=i.next
            count+=1

    def remove_by_value(self,value):
        if self.head is None:
            return
        if self.head.data ==value:
            self.head=self.head.next
            return
        i = self.head
        while i.next:
            if i.next.data==value:
                i.next=i.next.next
                break
            i=i.next
    def print(self):
        if self.head is None:
            print("Linked List is Empty")
        i=self.head
        llstr=''
        while i:
            llstr=llstr + str(i.data)+'==>'
            i=i.next
        print(llstr)

l1=LinkedList()
# # l1.print()
# l1.insert_at_begining(5)
# print(hex(id(l1)))
# l1.print()
# print(type(l1))
# l1.insert_at_begining(15) 
# l1.print()
# l1.insert_at_begining(25)
# l1.print()
l1.insert_lots_value([1,2,3,4,5,6,7,8,9,10])
l1.print()
l1.remove_by_value(8)
l1.print()
# print(l1.get_length())
# l1.remove_at(6)
# l1.print()
# l1.insert_at(6,7)
# l1.print()