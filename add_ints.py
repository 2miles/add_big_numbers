#!/usr/bin/env python3
import sys

# TODO output result as a stirng of digits 
# TODO Generalize add_big_numbers 
#       - take an array of inputs to add instead of just 2
# TODO Write a README.md explaining the program
#       - Also explain what I learned about python
#       - Analyze time and space complexity 


# INPUT: Array of lists
# RETURNS: size of largest list in the input array
def find_max_length(arr) :
    max = 0
    for i in range(len(arr)) :
        if(len(arr[i]) >= max) :
            max = len(arr[i])
    return max
        
# INPUT: Array of strings, start index
# OUTPUT: Copy of input array but with all the string reversed,
def reverse_args(arr, start=0) :
    result = []  
    for i in range(start,len(arr)) :
        result.append(arr[i][::-1])
    return result

# INPUT : Array of strings
# OUTPUT : Mutate array so its lists of chars instead of strings
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
    convert_to_list(argv_reversed)
    pad_smallest_general(argv_reversed)
    print(argv_reversed)

    result = add_big_numbers(argv_reversed[0], argv_reversed[1])
    print(result)

    return

if __name__ == '__main__' :
    main()