
def search(lst, value):

   temp = lst.get_head()

   if(lst.is_empty()):
       return False 
   else:
       while(temp.next_element):
            if(temp.data==value):
               return True
            else:
                temp=temp.next_element
       return False
