    res=[]
    lst1.sort()
    lst2.sort()
    i=0
    j=0
    while i<len(lst1) and j<len(lst2):
        if lst1[i]==lst2[j]:
            res.append(lst1[i])
            i+=1
            res.append(lst2[j])
            j+=1
        elif lst1[i]<lst2[j]:
            res.append(lst1[i])
            i+=1
        else:
            res.append(lst2[j])
            j=j+1
    for j in range(len(lst1)):
        print(j)
    if (i<len(lst1)):
       for l in range(j,len(lst1)):
          res.append(lst1[l])
    if (j<len(lst2)):
       for k in range(j,len(lst2)):
          res.append(lst2[k])
    return res
