def detect_loop(lst):
    first_point = lst.get_head() #create a pointer ie slow pointer
    second_point = lst.get_head() #create a pointer ie fast pointer that iterates twice as slow pointer

    while first_point and second_point and second_point.next_element:
        first_point =first_point.next_element
        second_point = second_point.next_element.next_element 

        if(first_point==second_point):#if two pointers lie on same node
            return True
    return False
