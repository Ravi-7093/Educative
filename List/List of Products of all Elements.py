def find_sum(lst, k):
    res=[]
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if(lst[i]+lst[j]==k):
                  res.append(lst[i])
                  res.append(lst[j])
                  return res
