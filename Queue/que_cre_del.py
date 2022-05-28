class Queue:
   def __init__(self):
     self.size =10
     self.front=-1
     self.rear=-1
     self.arr=[None]*self.size
  
   def Enqueue(self,data):
       if(self.rear==self.size-1):
           print("Queue is Full or Overflow")

       else:
            if(self.front==-1):
                self.front=0
            self.rear = self.rear+1
            self.arr[self.rear]=data
       return self.arr 

   def print(self):
       for i in self.arr:
           print(i)

 
   def Dequeue(self):
        if(self.rear == 1 or self.front>self.rear):
            print("Queue is Empty or Undeflow")
        else:
            x=self.front
            self.arr.pop(x)
            self.front=self.front+1
        return self.arr

s = Queue()
s.Enqueue(9)
s.Enqueue(8)
s.Enqueue(88)
s.Enqueue(98)
s.print()
s.Dequeue()
s.print()
