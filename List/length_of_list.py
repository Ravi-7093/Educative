def length(lst):
    # Write - Your - Code
    temp =lst.get_head()
    count=0

    while(temp is not None):
        temp = temp.next_element
        count+=1
    return count
