# Write the algoritm using recursion

def recursive_bsearch(lst, el):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst)/2
        if lst[mid] == el:
            return True
        else:
            if el < lst[mid]:
                return recursive_bsearch(lst[:mid], el)
            else:
                return recursive_bsearch(lst[mid+1:], el)


test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print(recursive_bsearch(test_list, 27))