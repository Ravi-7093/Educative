from Stack import MyStack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


class NewQueue:
    def __init__(self):
        self.main_stack = MyStack() #Main Stack
        self.second_stack = MyStack() #Temp Stack 


    # Inserts Element in the Queue
    def enqueue(self, value):
        # Write your code here
        self.main_stack.push(value) #Push the elements to main stack 
        print(value,"Enqueued")
        return True 

    # Removes Element From Queue
    def dequeue(self):
        if self.main_stack.is_empty() and self.second_stack.is_empty(): #check if both the stack is empty
            return None
        else:
            while(self.main_stack.is_empty() is False ): #Pop elements from the main_stack
               self.second_stack.push(self.main_stack.pop()) #Push the elements popped from the main stack into secondary stack
            temp = self.second_stack.pop() #pop the element into temp
            print("Popped element", temp)
        return temp
