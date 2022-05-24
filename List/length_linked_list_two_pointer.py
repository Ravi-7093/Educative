
def find_mid(lst):
    # Write your code here
    first_point=lst.get_head()
    second_point=lst.get_head()
    while(second_point and second_point.next_element): #traverse until the last element 
        first_point = first_point.next_element
        second_point = second_point.next_element.next_element #logic is when the second pointer reaches the last element the fist pointer points to the mid element
    return first_point.data
