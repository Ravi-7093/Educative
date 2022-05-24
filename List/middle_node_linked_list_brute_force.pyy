from operator import truediv


class Node:

 def __init__(self,data):
    self.data=data
    self.flag=0
    self.next=0

class LinkedList:

    def push(self,head_pnt,new_data):
        new_node=Node(new_data)
        new_node.flag=0
        new_node.next=head_pnt
        head_pnt=new_node
        return head_pnt
  
    
    def print_list(self,h):
        if(h is None):
            print("List is empty")
            return False
        else:
            temp =h
            while(temp.next is not None):
                print(temp.data,end="->")
                temp=temp.next
            print(temp.data, "-> None")
            return True
            
    def get_middle(self,h):
        temp = h
        count = 0

        while(temp is not None):
            count=count+1
            temp=temp.next

        mid=count//2
        temp =h
        for _ in range(mid):
             temp =temp.next
        return temp.data
            
    
lst= LinkedList()
head=None
head=lst.push(head,10)
head=lst.push(head,20)
head=lst.push(head,30)
head=lst.push(head,40)

lst.print_list(head)
print(lst.get_middle(head))
