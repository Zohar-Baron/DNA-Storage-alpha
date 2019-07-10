#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: repeatition_code
# Project: DNA-Storage-alpha
# Author: Zohar Baron
# Email: zoharbaron2002@gmail.com
# Created: 08/07/2019 14:33

"""this function will devide the ??? of dna to couples and for each couple
it will add another char (by the dictionary).
param:??? maybe to change back what i added to 3(deviding to oligos) to the begining of 5?
rerturn: ???"""

import math
def encod(word):
    groups_of_4_list = [word[4*i:4*i+4] for i in range(int(math.ceil(len(word)/4)))]
    encoded_msg = ''
    value_dict = {'A':2, 'T':3, 'C':4, 'G':5}
    for group in groups_of_4_list:
        p1 = value_dict[group[0]] + value_dict[group[1]] + value_dict[group[3]]
        p2 = value_dict[group[0]] + value_dict[group[2]] + value_dict[group[3]]
        p3 = value_dict[group[1]] + value_dict[group[2]] + value_dict[group[3]]
        encoded_msg += group
        if p1 % 4 == 0:
            encoded_msg += 'A'
        elif p1 % 4 == 1:
           encoded_msg += 'T'
        elif p1 % 4 == 2:
            encoded_msg += 'C'
        else:
            encoded_msg += 'G'
        if p2 % 4 == 0:
            encoded_msg += 'A'
        elif p2 % 4 == 1:
            encoded_msg += 'T'
        elif p2 % 4 == 2:
            encoded_msg += 'C'
        else:
            encoded_msg += 'G'
        if p3 % 4 == 0:
            encoded_msg += 'A'
        elif p3 % 4 == 1:
            encoded_msg += 'T'
        elif p3 % 4 == 2:
            encoded_msg += 'C'
        else:
            encoded_msg += 'G'
    return encoded_msg



def decod(msg):
    groups_of_7_list = [msg[7*i:7*i+7] for i in range(int(math.ceil(len(msg)/7)))]
    final_msg = ''
    for group in groups_of_7_list:
        z1 = value_dict[group[0]] + value_dict[group[1]] + value_dict[group[3]]
        z2 = value_dict[group[0]] + value_dict[group[2]] + value_dict[group[3]]
        z3 = value_dict[group[1]] + value_dict[group[2]] + value_dict[group[3]]
        if z1 % 4 == 0:
            z1 = 'A'
        elif z1 % 4 == 1:
           z1 = 'T'
        elif z1 % 4 == 2:
            z1 = 'C'
        else:
            z1 = 'G'
        if z2 % 4 == 0:
            z2 = 'A'
        elif z2 % 4 == 1:
            z2 = 'T'
        elif z2 % 4 == 2:
            z2 = 'C'
        else:
            z2 = 'G'
        if z3 % 4 == 0:
            z3 = 'A'
        elif z3 % 4 == 1:
            encoded_msg = 'T'
        elif z3 % 4 == 2:
            z3 = 'C'
        else:
            z3 = 'G'
        p1 = group[4]
        p2 = group[5]
        p3 = group[6]
        if p1 == z1 and p2 == z2 and p3 != z3 or p1 == z1 and p2 != z2 and p3 == z3 or p1 != z1 and p2 == z2 and p3 == z3 or p1 == z1 and p2 == z2 and p3 == z3:
            final_msg += group[0:4]
        elif p1 != z1 and p2 != z2 and p2 != z3:
            final_msg += group[0:3]
            #________
        elif p1 != z1 and p2 != z2 and p3 == z3:
            #________
            final_msg += group[1: 4]
        elif p1 != z1 and p2 == z2 and p3 != z3:
            final_msg += group[0]
            #________
            final_msg += group[2:4]
        else:
            final_msg += group[0:2]
            #________
            final_msg += group[3]
    print(final_msg)
    return final_msg

#msg = 'ACGTTCAACGTTCA'