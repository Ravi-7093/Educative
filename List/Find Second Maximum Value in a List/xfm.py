def find_second_maximum(lst):
    # Write your code here
    lst.sort(reverse=True)
    return lst[1]
