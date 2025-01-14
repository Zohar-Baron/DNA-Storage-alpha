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

def encode(msg,r):
    out_msg = ''
    for char in msg:
        out_msg += r*char
    return out_msg


"""this function will decode from binari with corecting mistake code to the original code (hopfuly) 
paremeter_1: the encoded msg = word
type_parameter_1: str
return: str of the hopfuly original msg"""

def decode(word,r):
    groups_of_3_list = [word[r*i:r*i+r] for i in range(int(math.ceil(len(word)/r)))]
    original_msg = ''
    for group in groups_of_3_list:
        if len(group) != r:
            continue
        sum = int(group[0]) + int(group[1]) + int(group[2])
        if sum >1:
            original_msg += '1'
        else:
            original_msg += '0'
    return original_msg