class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next =None
class Queue:
    def __init__(self):
        self.front = None #2 pointers
        self.rear = None

    def Enqueue(self,data):
         new_node = Node(data)
         if(self.rear is None): #if rear is none point the 2 pointers to the first node inserted
             self.front = new_node
             self.rear = new_node
             return 

         self.rear.next = new_node # insert the element next to the element inserted at first
         self.rear = new_node # point rear to new node
    
    def Dequeue(self):
         if(self.front is None): # check if front is null
             return 
         temp =self.front # create a pointer
         self.front =temp.next # assign the front to next element of element deleted 
        


         
    def print(self):

        temp= self.front  
        while temp.next is not None:
             print(temp.data, end=" -> ")
             temp = temp.next
        print(temp.data, "-> None")
u = Queue()
u.Enqueue(6)
u.Enqueue(89)
u.Enqueue(99)
#u.print()
u.Dequeue()
u.print()

        
