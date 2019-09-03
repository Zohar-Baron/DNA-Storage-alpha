#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: two_bits_3
# Project: DNA-Storage-alpha
# Author: Zohar Baron
# Email: anavy (at) technion (dot) ac (dot) il
# Created: 01/07/2019 15:49
""" this function wil translate the binary code to dna code' seperate it to oligosnokleotides
param_1: msg_encoded: str of encoded binar code.
return: str of dna."""


import math
def bin2dna(msg_encoded):
    msg_divide_list = [msg_encoded[2*i:2*i+2] for i in range(int(math.ceil(len(msg_encoded)/2)))]
    output = ''
    translator = {'01': 'T', '10': 'A', '00': 'G', '11': 'C'}
    for pair in msg_divide_list:
        output += translator[pair]
    print(output)
    return output


"""this function do the oposite from the one above, it translate from DNA code to binari code.
param_1: str of dna (came out from the sequencer or from 4) not seperated
return: str of binar code, with or without code against mistakes in it."""
def dna2bin(msg):
    #print(msg)
    output = ''
    translator2= {'T': '01', 'A': '10', 'G': '00', 'C': '11'}
    for letter in msg:
        output += translator2[letter]
    return output