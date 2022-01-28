#!/usr/bin/env python3

import sys


# INPUTS: Array, Start index
def print_array(arr, start=0) :
    for i in range(start, len(arr)):
        print(arr[i], end = ' ')

# INPUT: array of lists
# RETURNS: number of elemtents of the largest list in the array
def find_max_length(arr) :
    max = 0
    for i in range(len(arr)) :
        if(len(arr[i]) >= max) :
            max = len(arr[i])
    return max
        


# INPUTS: Array of strings
# OUTPUT: Array of lists of chars,
# where each list represents the corrisponding string in reverse
def reverse_args(arr, start=0) :
    result = []  
    for i in range(start,len(arr)) :
        result.append(arr[i][::-1])
    return result

# INPUT : array of strings
# OUTPUT : array of lists-of-chars
def convert_to_list(arr) :
    for i in range(len(arr)) :
        arr[i] = list(arr[i])

# RETURNS integer sum of all command line arguments 
def sum_elem(arg_arr, start=0) :
    sum = 0
    for i in range(start,len(arg_arr)):
        sum += int(arg_arr[i])
    return sum


# INPUT: array of lists-of-chars
# OUTPUT: array elements so that they are all the same length
# by padding the ends of the shorter ones with '0's.
def pad_smallest_general(arr) :
    max = find_max_length(arr)
    for i in range(len(arr)) :
        while len(arr[i]) < max :
            arr[i].append('0')

# takes two lists of chars and if one is shorter it pads it with '0's.
# So that both lists are the same size
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

   
# Add two numbers grade school style.
# assuming the 'numbers' are given as lists of chars where
# the digits have been reversed and the smaller one has been 
# padded with zeros
def add_big_numbers(list1, list2) :
    result = []
    temp = 0

    for i in range(len(list1)) :
        total = (int(list1[i]) + int(list2[i]) + temp) 
        result.append(total % 10)    
        temp = total // 10
    if(temp != 0) :
        result.append(temp)
    return result 


# main
def main() :
    argv_reversed = reverse_args(sys.argv, 1)
    print(argv_reversed)
    convert_to_list(argv_reversed)
    print(argv_reversed)
    print(find_max_length(argv_reversed))
    pad_smallest_general(argv_reversed)
    print(argv_reversed)

    # padded_char_lists = pad_smallest(reverse_args[0], reverse_args[1])
    # print_array(padded_char_lists)
    return

if __name__ == '__main__' :
    main()