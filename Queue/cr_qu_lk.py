class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class CircQ:
    def __init__(self) -> None:
        self.front=None
        self.rear =None
        #self.size=5

    def Enqueue(self,data):
        new_node =Node(data)
        if(self.rear==None):
          self.rear=new_node
          self.front=new_node
          return
        #elif(((self.count+1)%self.size)==0):
            #print("Queue is full")
        else:
            self.rear.next=new_node #attach new node to next of rear elemt 
        self.rear =new_node #point rear to new node 
        new_node.next=self.front # point the new_node pointer point to front since circular queue #check gfg for detailed explanation
    
    def Dequeue(self): 
        if(self.front == None): #if front is none 
            print("Queue is empty")
        elif(self.front==self.rear):#check for only one element in the queue 
            temp =self.front.data
            self.front=None
            self.rear =None
        else :
            temp =self.front #pointer to point at the front 
            value =temp.data
            self.front = self.front.next #move front to point to the node next to deleted node  
            self.rear.next = self.front #update rear to point new front 
            return value



    def printData(self):
        temp = self.front
        #print("The circular queue elements are ",end=" ")
        while temp.next != self.front: # important until circular print all the elements 
            print(temp.data,end="->")
            temp =temp.next
        print(temp.data)



c=CircQ()
c.Enqueue(8)
c.Enqueue(9)
c.Enqueue(10)
c.printData()
c.Dequeue()

c.printData()			
