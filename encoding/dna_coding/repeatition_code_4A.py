#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: repeatition_code
# Project: DNA-Storage-alpha
# Author: Leon Anavy
# Email: anavy (at) technion (dot) ac (dot) il
# Created: 01/07/2019 03:40

"""this function take each char from a str of DNA and multiply it by 3 (maybe it wil be parameter)
param: str of DNA
returns str of DNA longer* 3."""
import math
#########לשנות לקבוצות!!!!!
def encode(msg):
    out_msg = ''
    for char in msg:
        out_msg += 3*char
    return out_msg


"""this function do the oposite from the one above, 
it takes a str of DNA and returns it without the multiple characters an without mistakes (hopfully)
param: str of DNA came out from the sequencer
return: str of shorter DNA"""
def decode(word):
    groups_of_3_list = [word[3*i:3*i+3] for i in range(int(math.ceil(len(word)/3)))]
    original_msg = ''
    for group in groups_of_3_list:
        if group[0] == group[1] and group[1] == group[2]:
            original_msg += group[0]
        elif group[0] != group[1] and group[1]== group[2]:
            original_msg += group[1]
        elif group[0] != group[1] and group[0] == group[2]:
            original_msg += group[0]
        else:
            original_msg += group[0]
    return original_msg