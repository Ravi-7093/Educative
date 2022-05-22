class Node:
    def __init__(self,data):
        self.data=data
        self.nextElement=None
    
class Linked_List:
    def __init__(self):
        self.head=None #initally head is null 

    def insert_at_front(self,data):
        new_node=Node(data) #creation of new Node 
        new_node.nextElement=self.head #point new node next ele to head (backwards)
        self.head=new_node #point head to new_node
        return self.head #return head

    def append(self,place_to_insert,new_data):
        new_node= Node(new_data)
        prev =self.head
        if prev is None: #checking for no node in list
            print("no previous nodes exists in linked list")
            return 
        while (prev.nextElement is not None):
            if prev.data==place_to_insert:
                 new_node.nextElement = prev.nextElement #creating a link to new node and the previous node next element
                 prev.nextElement = new_node #pointing previous node pointer to new node
                 return True
            else:
                prev=prev.nextElement
          
   
    def push(self,data):
        
        new_node = Node(data)
        if self.head is None: #check if no node 
            self.head= new_node
        
        last = self.head #new pointer to traverse the list 
        while(last.nextElement): #till we get the last element traverse the list 
            last=last.nextElement 
        last.nextElement =new_node #assign new node 
    
    def isEmpty(self):
        if self.head is None:
           return True
        else:
           return False
    
    def printlist(self):
        if(self.isEmpty()):
            print("list is empty")
            return False
        temp=self.head
        while temp.nextElement is not None:
             print(temp.data, end=" -> ")
             temp = temp.nextElement
        print(temp.data, "-> None")
        return True

list = Linked_List()
list.printlist()
list.insert_at_front(1)
list.insert_at_front(3)

list.insert_at_front(2)

list.insert_at_front(13)
list.insert_at_front(6)
list.printlist()
list.append(3,4)
list.printlist()
list.push(8)
list.printlist()

#list.insert_at_front(11)

        
        
