def right_rotate(lst, k):
    # Write your code here
    if len(lst)==0:#check for length of the array
        k=0
    else:
        k = k%len(lst) #check the value for k
    new_lst=[]
    for i in range(len(lst)-k,len(lst)):#check for the start of the list
        print(i)
        new_lst.append(lst[i])#append values for the new_lst
    for i in range(0,len(lst)-k):#append the rest of the values to new_lst
        new_lst.append(lst[i])
    return new_lst#return the new_lst ie after right rotation 
