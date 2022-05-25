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
        new_node.prev=None # Point the previous pointer of new node to null
        new_node.next = self.head # new_node next points to the next node 
        if(self.head is not None):
            self.head.prev = new_node # if there is more than one node prev node points to new_node
        self.head = new_node# move the head pointer to point to new node 
    
