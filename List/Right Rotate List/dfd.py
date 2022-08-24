def right_rotate(lst, k):
    # Write your code here
    if len(lst)==0:
        k=0
    else:
        k = k%len(lst)
    new_lst=[]
    for i in range(len(lst)-k,len(lst)):
        print(i)
        new_lst.append(lst[i])
    for i in range(0,len(lst)-k):
        new_lst.append(lst[i])
    return new_lst
