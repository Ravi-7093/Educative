class Node():
    def __init__(self,val):
      self.val=val #initalize the val for the node 
      self.next=None#initialize the next to None 
    def get_next(self):
      return self.next#getters and setters pointer for Node class
    def set_next(self,next):
      self.next=next
    def get_val(self):#getters and setters for data for Node class
      return self.val
    def set_val(self,next):
      self.val=val
        
class Linked_List():
    def __init__(self,head=None):
      self.head=head #intialize the head to point to None
      self.count=0#counter to track the number of nodes in the linked list 
      
    def insert(self,data):
      new_node=Node(data)#create an empty noode 
      new_node.set_next(self.head)#point the new_node next to head
      self.head=new_node#point the head to the new_node 
      self.count+=1#increment the counter 
      
    def get_nodes(self):
      return self.count #check for the counter 
      
    def is_empty(self):
      return self.head==None#check if head is None then the linked list is empty 
      
    def print_nodes(self):
        if(self.is_empty()):#check if the linked list is empty 
            return False#else return False 
        temp=self.head#store the head to temp
        while temp.next is not None:#traverese until the final node is found in the linked list 
             #print(temp.val,end='->')
             temp=temp.next
        print(temp.val,"-> None")
        return True
        
    def find(self,data):#check for node in linked list 
        item=self.head #point the item 
        while item is not None:#traverse the linked list until nodes are present 
            if item.get_val()==data:#if item found return the value 
                return item.get_val()
            else:
                item=item.get_next()
        return False#else return False
        
    def remove(self,data):
        
        current =self.head#point the current to the node
        prev=None#prev is None 
        
        while current is not None:#traverse the linked list until nodes are present 
            if current.get_val()==data:#if the current pointer has value break
                break
            prev=current #point the current to previoud 
            current=current.get_next()#point the current to next element 
            print(current.get_val())#get the current value 
        if prev is None:#if prev is None then the head is our element 
            self.head = current.get_next()#then we move the head it point next 
            self.count -= 1#decrement the count 
        if current is None:
            print("No element was found ")
        else:
            prev.set_next(current.get_next())#break the linking ie point the previous to the current node's next 
            self.count-=1#decrement the pointer 
        
c = Linked_List()
c.insert(20)
c.insert(30)
c.insert(40)
c.insert(50)
c.insert(60)
#c.print_nodes()
#print(c.find(40))
c.remove(20)
c.print_nodes()        
        
