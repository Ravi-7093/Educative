class Node:

 def __init__(self,data):
    self.data=data 
    self.flag=0 
    self.next=0

class LinkedList:

    def push(self,head_pnt,new_data):
   
        new_node=Node(new_data) #new node creation
        new_node.flag=0
        new_node.next=head_pnt #make the next pointer to point to previous node
        head_pnt=new_node #make te head point to new node 
        return head_pnt #return the head pointer 
    
    def detect_cycle(self,h):
        while h is not None: #if head is not None 

            if(h.flag==1): #if the node is already traversed once 
                return True
            h.flag=1 #make flag as one
            h = h.next 
        return False
    
    def print_list(self,h):
        if(h is None):
            print("List is empty")#list is not empty
            return False
        else:
            temp =h #create a pointer 
            while(temp.next is not None):
                print(temp.data,end="->")
                temp=temp.next
            print(temp.data, "-> None")
            return True
    
lst= LinkedList()
head=None
head=lst.push(head,10)
head=lst.push(head,20)
head=lst.push(head,30)
lst.print_list(head)

head.next.next.next = head #important step for creating the loop
print(lst.detect_cycle(head))
