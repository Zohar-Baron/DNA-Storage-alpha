#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: repeatition_code
# Project: DNA-Storage-alpha
# Author: Leon Anavy
# Email: anavy (at) technion (dot) ac (dot) il
#created: 03/07/19 15:15
"""this function will devide the binari str to groups of 4, and add nums by hamming code dict
param_1: str of regular binari code
return: str of binari + hamming code. """

import math
def encode(msg):
    #print(msg)#
    groups_of_4_list = [msg[4*i:4*i+4] for i in range(int(math.ceil(len(msg)/4)))]
    if len(groups_of_4_list[-1]) == 1:
        groups_of_4_list[-1] += '000'
        with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\results.txt', 'w') as f:
            f.write('in 2B ecnode, added "000" /n')
        num_of_added_0 = 3 
    elif len(groups_of_4_list[-1]) == 2:
        groups_of_4_list[-1] += '00'
        with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\results.txt', 'w') as f:
            f.write('in 2B encode, added "00" /n')
        num_of_added_0 = 2
    else:
        groups_of_4_list[-1] += '0'
        with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\results.txt', 'w') as f:
            f.write('in 2B encode, added "0" /n')
        num_of_added_0 = 1
    encoded_msg = ''
    for group in groups_of_4_list:
        p1 = int(group[0]) + int(group[1]) + int(group[3])
        p2 = int(group[0]) + int(group[2]) + int(group[3])
        p3 = int(group[1]) + int(group[2]) + int(group[3])
        encoded_msg += group
        if p1 % 2 == 0:
            encoded_msg += '0'
        else:
           encoded_msg += '1'
        if p2 % 2 == 0:
            encoded_msg += '0'
        else:
           encoded_msg += '1'
        if p3 % 2 == 0:
            encoded_msg += '0'
        else:
           encoded_msg += '1'
    return encoded_msg , num_of_added_0
#msg = '001101011010'
#encode(msg)


"""this function do the oposite from the one above, it should find the mistakes and fixed them.
it devide the str to groups of 7, for each group cheks if the sums of each 3 nums out of 4 
is correct acording to the answer that placed at the last 3 chars (from the 7). 
param: str of binari code, came out from 3
return: str of binari shorter and without mistakes hopefuly"""
def decode(word, num_of_added_0):
    #print(word) #
    groups_of_7_list = [word[7*i:7*i+7] for i in range(int(math.ceil(len(word)/7)))]
    #print(groups_of_7_list) #
    output = ''
    for group in groups_of_7_list:
        if len(group) != 7:
            continue
        sum_t1 = int(group[0]) + int(group[1]) + int(group[3])
        sum_t2 = int(group[0]) + int(group[2]) + int(group[3])
        sum_t3 = int(group[1]) + int(group[2]) + int(group[3])
        #print(sum_t1,  sum_t2, sum_t3)
        if sum_t1 % 2 == 0:
            z1 = '0'
        else:
            z1 = '1'
        if sum_t2 % 2 == 0:
            z2 = '0'
        else:
            z2 = '1'
        if sum_t3 % 2 == 0:
            z3 = '0'
        else:
            z3 = '1'
        #print(z1,  z2, z3)
        p1 = group[4]
        p2 = group[5]
        p3 = group[6]
        if p1 == z1 and p2 == z2 and p3 != z3 or p1 == z1 and p2 != z2 and p3 == z3 or p1 != z1 and p2 == z2 and p3 == z3 or p1 == z1 and p2 == z2 and p3 == z3:
            output += group[0:4]
            #print("nothing is wrong")
        elif p1 != z1 and p2 != z2 and p2 != z3:
            #print("the problem is on the forth")
            output += group[0:3]
            if group[3] == '0':
                output += '1'
            else:
                output += '0'
        elif p1 != z1 and p2 != z2 and p3 == z3:
            #print("the problem is on the first")
            if group[0] == '0':
                output += '1'
            else: 
                output += '0'
            output += group[1: 4]
        elif p1 != z1 and p2 == z2 and p3 != z3:
            #print("the problem is on the second")
            output += group[0]
            if group[1] == '0':
                output += '1'
            else:
                output += '0'
            output += group[2:4]
        else:
            #print("the problem is on the third")
            output += group[0:2]
            if group[2] == '0':
                output += '1'
            else:
                output += '0'
            output += group[3]
    if num_of_added_0 != 0:
        output = output[:-num_of_added_0]            
    #print(output)
    return output

#word = '001110001010101010101'
#decode(word)
 