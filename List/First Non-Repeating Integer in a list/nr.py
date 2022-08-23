def find_first_unique(lst):
    # Write your code here
    d={} #empty dictionary 
    for i in range(len(lst)):
        d[lst[i]]=d.get(lst[i],0)+1 #store the occurences of each character 
    print(d)
    for key, value in d.items():#for each value in key,value in dictionary 
        if value==1:#check if value ==1 
            return key#return the key 
        
    
