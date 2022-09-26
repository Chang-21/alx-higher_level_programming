#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
#if idx idx is negative print the original list
    if idx < 0:
        return idx
#if idx is greater than the number of elements in my list print my_list
    elif idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
