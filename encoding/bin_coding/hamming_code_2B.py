#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: repeatition_code
# Project: DNA-Storage-alpha
# Author: Leon Anavy
# Email: anavy (at) technion (dot) ac (dot) il
#created: 03/07/19 15:15
""" """

import math
def encode(msg):
    groups_of_4_list = [msg[4*i:4*i+4] for i in range(int(math.ceil(len(msg)/4)))]
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
    return encoded_msg
#msg = '001101011010'
#encode(msg)



def decode(word):
    groups_of_7_list = [word[7*i:7*i+7] for i in range(int(math.ceil(len(word)/7)))]
    output = ''
    for group in groups_of_7_list:
        sum_z1 = int(group[0]) + int(group[1]) + int(group[3])
        sum_z2 = int(group[0]) + int(group[2]) + int(group[3])
        sum_z3 = int(group[1]) + int(group[2]) + int(group[3])
        if sum_z1 % 2 == 0:
            z1 = '0'
        else:
            z1 = '1'
        if sum_z2 % 2 == 0:
            z2 = '0'
        else:
            z2 = '1'
        if sum_z3 % 2 == 0:
            z3 = '0'
        else:
            z3 = '1'
        p1 = group[4]
        p2 = group[5]
        p3 = group[6]
        if p1 == z1 and p2 == z2 and p3 != z3 or p1 == z1 and p2 != z2 and p3 == z3 or p1 != z1 and p2 == z2 and p3 == z3 or p1 == z1 and p2 == z2 and p3 == z3:
            output += group[0:4]
        elif p1 != z1 and p2 != z2 and p2 != z3:
            output += group[0:3]
            if group[3] == '0':
                output += '1'
            else:
                output += '0'
        elif p1 != z1 and p2 != z2 and p3 == z3:
            if group[0] == '0':
                output += '1'
            else: 
                output += '0'
            output += group[1: 4]
        elif p1 != z1 and p2 == z2 and p3 != z3:
            output += group[0]
            if group[1] == '0':
                output += '1'
            else:
                output += '0'
            output += group[2:4]
        else:
            output += group[0:2]
            if group[2] == '0':
                output += '1'
            else:
                output += '0'
            output += group[3]
    print(output)
    return output

word = '001110001010101010101'
decode(word)
 