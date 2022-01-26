#!/usr/bin/env python3

import sys

print ('Number of args: ', len(sys.argv), 'args.')
print ('The first arg: ', sys.argv[0])
print ('The second arg: ', sys.argv[1])
print ('The second arg: ', sys.argv[2])

sum = 0
for i in range(1,len(sys.argv)):
    sum += int(sys.argv[i])
print ('The sum of the numbers entered is: ', sum)