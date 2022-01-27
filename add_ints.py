#!/usr/bin/env python3

import sys

# print arr from start
def print_array(arr, start) :
    for i in range(start, len(arr)):
        print(arr[i], end = ' ')

# INPUT: an argv array
# OUTPUT: an array with each of the given args (not the 0th) reversed
def reverse_each_arg(arr, start) :
    result = []  
    for i in range(start,len(arr)) :
        result.append(arr[i][::-1])
    return result

# sum the elements(as integers) of arr starting from start
def sum_elem(arr, start) :
    sum = 0
    for i in range(start,len(arr)):
        sum += int(arr[i])
    return sum



def main() :
    print ('Sum of the arguments: ', sum_elem(sys.argv, 1))
    new_array = reverse_each_arg(sys.argv, 1)
    print ('All the arguments reversed: ')
    print_array(new_array, 0)
    return

if __name__ == '__main__' :
    main()