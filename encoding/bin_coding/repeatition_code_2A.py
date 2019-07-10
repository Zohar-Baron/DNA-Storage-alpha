#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: repeatition_code
# Project: DNA-Storage-alpha
# Author: Zohar Baron
# Email: zoharbaron2002@gmail (dot) com
# Created: 01/07/2019 14:37
"""this function will do the first coding option wich is repeat code.the function will devided the str into groups of 4,
and each group will be multiply in 3. it will be written as list with the groups inside it, at the end it will chainged into str. 
parmeter_1: file0 (file_rows)/ msg 
type: str
return: str"""
import math

def encode(msg):
    out_msg = ''
    for char in msg:
        out_msg += 3*char
    return out_msg


"""this function will decode frim binari with corecting mistake code to the original code (hopfuly) 
paremeter_1: the encoded msg
type_paramete_1: str
return: str of the hopfuly original msg"""

def decode(word):
    groups_of_3_list = [word[3*i:3*i+3] for i in range(int(math.ceil(len(word)/3)))]
    #added zeros and i need to figure ouut a way to "rememeber" take it down a the end.
    if len(groups_of_3_list[-1]) == 1:
        groups_of_3_list[-1] += '00'
    if len(groups_of_3_list[-1]) == 2:
        groups_of_3_list[-1] += '0'
    #
    original_msg = ''
    for group in groups_of_3_list:
        sum = int(group[0]) + int(group[1]) + int(group[2])
        if sum >1:
            original_msg += '1'
        else:
            original_msg += '0'
    return original_msg