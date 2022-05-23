from ast import Return
from multiprocessing.dummy import current_process
from os import preadv


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Linked_List:
    def __init__(self):
        self.head=None #initally head is null 

    def insert_at_front(self,data):
        new_node=Node(data) #creation of new Node 
        new_node.next=self.head #point new node next ele to head (backwards)
        self.head=new_node #point head to new_node
        return self.head #return head

    def append(self,place_to_insert,new_data):
        new_node= Node(new_data)
        prev =self.head
        if prev is None: #checking for no node in list
            print("no previous nodes exists in linked list")
            return 
        while (prev.next is not None):
            if prev.data==place_to_insert:
                 new_node.next = prev.next #creating a link to new node and the previous node next element
                 prev.next = new_node #pointing previous node pointer to new node
                 return True
            else:
                prev=prev.next
          
   
    def push(self,data):
        
        new_node = Node(data)
        if self.head is None: #check if no node 
            self.head= new_node
        
        last = self.head #new pointer to traverse the list 
        while(last.next): #till we get the last element traverse the list 
            last=last.next 
        last.next =new_node #assign new node 
    
    def isEmpty(self):
        if self.head is None:
           return True
        else:
           return False
    
    def delete_at_front(self):
        if(self.isEmpty()):#check list is empty
            return False
        else:
            temp=self.head#get head
            if(temp is not None): #if temp is not none
                self.head=temp.next #move head next element 
                temp.next=None#remove the first elemnt
                return True

    def delete_at_rear(self):
        if(self.head is not None):#check if head is none
            if(self.head.next is None): #check if more than 1 element exists
                self.head=None
            else:
                temp = self.head
                while(temp.next.next != None):#traverse to the second last element in the list
                       temp = temp.next
                lastNode = temp.next# point to last element 
                temp.next = None #ensure the pointer to second last element is null
                lastNode = None
   
    def del_by_val(self,data):
        temp=self.head #Access the head
        prev=None #create a  pointer
        if(self.isEmpty()):#check if the list exists
            return False
        else:
            if temp.data is data: #check if the head points to given element
                self.delete_at_front()#delete at front
            else:
                while temp is not None:#traverse the list 
                    if temp.data is data: #check for the element
                        prev.next = temp.next
                        temp.next= None
                        return True
                    prev =temp #loop till you get the element specified
                    temp = temp.next


    def reverse(self):
        prev=None # create a pointer to point to previous node
        curr = self.head #pointer to traverse the list
        next =None  # create a pointer to point to next node
        while(curr is not None):
            next = curr.next #next is pointing to next element in head
            curr.next =prev #prev is pointing to null intially important step for reversing
            prev =curr 
            curr=next
        self.head =prev # pointing the last node as head

          


    def printlist(self):
        if(self.isEmpty()):
            print("list is empty")
            return False
        temp=self.head
        while temp.next is not None:
             print(temp.data, end=" -> ")
             temp = temp.next
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
#list.printlist()
list.push(8)
list.printlist()
#list.insert_at_front(11)
#list.delete_at_front()
#list.printlist()
#list.delete_at_rear()
#list.printlist()
#list.del_by_val(3)
#list.printlist()
list.reverse()
list.printlist()

        
