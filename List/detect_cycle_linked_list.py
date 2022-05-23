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
    
    def detect_cycle(self,h):
        while h is not None:

            if(h.flag==1):
                return True
            h.flag=1
            h = h.next
        return False
    
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
    
lst= LinkedList()
head=None
head=lst.push(head,10)
head=lst.push(head,20)
head=lst.push(head,30)
lst.print_list(head)

head.next.next.next = head
print(lst.detect_cycle(head))
