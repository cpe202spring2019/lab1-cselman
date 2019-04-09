
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    try:
        if len(int_list) == 0:
            return None
        else:
            max_val = int_list[0]
            for x in int_list:
                if x > max_val:
                    max_val = x
            return max_val
    except:
        raise ValueError


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    elif len(int_list) == 0:
        return []
    return [int_list[len(int_list) - 1]] + reverse_rec(int_list[:(len(int_list) - 1)])


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if len(int_list) == 0:
        raise ValueError
    try:
        mid = (low + high) // 2
        if target < int_list[mid]:
            high = mid - 1
            return bin_search(target, low, high, int_list)
        elif target > int_list[mid]:
            low = low + 1
            return bin_search(target, low, high, int_list)
        elif target == int_list[mid]:
            return mid
    except IndexError:
        return None
