#!/usr/bin/env python3

import sys

# print arr from start
def print_array(arr, start) :
    for i in range(start, len(arr)):
        print(arr[i], end = ' ')

# INPUT: String array, starting point
# OUTPUT: String array with each element reversed 
def reverse_each_arg(arr, start) :
    result = []  
    for i in range(start,len(arr)) :
        result.append(arr[i][::-1])
    return result

# sum the elements(as ints) of string array starting from start
# RETURNS sum as integer
def sum_elem(arr, start) :
    sum = 0
    for i in range(start,len(arr)):
        sum += int(arr[i])
    return sum


# takes two lists and if one is shorter it pads it with zeros.
# So that both lists are the same size, and one has trailing zeros
def pad_smallest(list1, list2) :
    len1 = len(list1)
    len2 = len(list2)
    if len1 != len2 :
        if len1 < len2 :
            diff = len2 - len1
            for i in range(diff) :
                list1.append('0')
        else :
            diff = len1 - len2
            for i in range(diff) :
                list2.append('0')

    


# main
def main() :
    print ('Sum of the arguments: ', sum_elem(sys.argv, 1))
    new_array = reverse_each_arg(sys.argv, 1)
    print ('All the arguments reversed: ')
    print_array(new_array, 0)

    list2 = ['1', '2']
    list1 = ['1', '2', '3', '4', '5', '5', '3']
    print('list1', list1)
    print('list2', list2)
    pad_smallest(list1,list2)
    print('list1 after', list1)
    print('list2 after', list2)

    return

if __name__ == '__main__' :
    main()