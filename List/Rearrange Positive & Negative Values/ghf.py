def rearrange(lst):
    # Write your code here
    pass
    ans=[]
    ans_two=[]
    for i in range(len(lst)):
        if lst[i]<0:
            ans.append(lst[i])
        else:
            ans_two.append(lst[i])
    return ans+ans_two
