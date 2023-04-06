# Given a sorted integer list of n elements and a target value. Write a function that searches for a target. If a target exist, return index; otherwise return -1

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

def sortedlst(lst, el):
    if len(lst) == 0:
        return -1
    else:
        mid = len(lst)//2
        if lst[mid] == el:
            return mid
        else:
            if el < lst[mid]:
                return sortedlst(lst[:mid],el)
            else:
                return sortedlst(lst[mid+1:], el)


print(sortedlst(test_list, 12))