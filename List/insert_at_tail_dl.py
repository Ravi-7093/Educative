class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
    
    def insert_at_head(self,new_data):

        new_node = Node(new_data)
        new_node.prev=None
        new_node.next = self.head
        if(self.head is not None):
            self.head.prev = new_node
        self.head = new_node
   
    
    def insert_at_tail(self,new_data):
       
        new_node = Node(new_data)
        temp = self.head
        while(temp.next is not None):
            temp=temp.next
        temp.next = new_node #point to new node for  previous last node 
        new_node.prev = temp #point to previous node 
        
lst =DoubleLinkedList()
lst.insert_at_head(9)
lst.insert_at_head(8)
lst.insert_at_head(11)
lst.insert_at_head(12)
lst.insert_at_tail(2)
lst.print_list(lst.head)
