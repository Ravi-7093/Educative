class CrQ():
  def __init__(self) -> None:
      self.front=-1
      self.rear=-1
      self.size = 5
      self.arr = [None]*self.size #Initalize the array element to zero

  def Enqueue(self,data):

      if(self.rear==-1):
          self.rear=0  #Intialize the rear to zero
          self.front=0 #Initalize the front to zero
          self.arr[self.rear]=data 
          return
      elif(((self.rear+1)%self.size)==self.front):#check if rear has traversed the list more than once i.e(circular)
          print("Queue is Full")
          return 
      else:
          self.rear=(self.rear+1)%self.size #increment rear for insertion of the element into the queue 
          self.arr[self.rear]=data 

  def Dequeue(self):
    
      if(self.rear==self.front): #check if there is only one element ie rear and front is equal to zero
          temp =self.arr[self.front] # store the element to be deleted into temp
          self.rear=-1 #decrease rear 
          self.front=-1 #decrease front 
          return temp

      elif((self.rear)and (self.front)==-1):#Check if Queue is empty 
          print("Queue is Underflow")
          exit()
      else:
          temp = self.arr[self.front] 
          self.front=((self.front+1)%self.size)
          return temp           


  def print(self):
      if(self.front==-1):
          print("Queue is empty")
      
      elif(self.rear>self.front):
           for i in range(self.front,self.rear+1):
              print(self.arr[i])
      else:
           for i in range(self.front,self.size):
               print(self.arr[i])


    
c = CrQ()
c.Enqueue(6)
#c.print()
c.Enqueue(7)
c.Enqueue(9)
#c.print()

#c.print()
c.Enqueue(0)
c.Enqueue(90)
#c.Enqueue(8)
#c.print()
c.Dequeue()
c.print()
