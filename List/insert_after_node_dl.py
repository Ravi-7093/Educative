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
    
    def insert_after(self,prev_node,new_data):

        new_node = Node(new_data) #Initalize the node 
        new_node.next=prev_node.next # new_node next element is  pointing to the previous node next element
        prev_node.next= new_node # previous node next element points to the new_node
        new_node.prev= prev_node # new_node previous points to the previous 

        if(new_node.next): # check if new_node exists
            new_node.next.prev = new_node #new_node next element previous point to new_node (all the pointers of 3 nodes are set correctly)
    
    def insert_at_tail(self,new_data):
       
        new_node = Node(new_data)
        temp = self.head
        while(temp.next is not None):
            temp=temp.next
        temp.next = new_node
        new_node.prev = temp





    def print_list(self,head):
        temp = head
        while(temp.next is not None):
            print(temp.data,end="->")
            temp=temp.next
        print(temp.data, "-> None")

lst =DoubleLinkedList()
lst.insert_at_head(9)
lst.insert_at_head(8)
lst.insert_at_head(11)
lst.insert_at_head(12)

lst.insert_after(lst.head.next,3)
lst.insert_at_tail(2)
lst.print_list(lst.head)

