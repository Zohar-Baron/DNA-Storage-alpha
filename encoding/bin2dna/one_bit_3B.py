#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: parameters
# Project: DNA-Storage-alpha
# Author: Zohar Baron
# Email: ZoharBaron2002@gmail.com
# Created: 29/07/2019 16:53

"""this functuon translate from bin to DNA by dividing to one bits and transating to letters avouding two in a line of same letter 
param_1: msg_encoded: str of encoded binar code.
return: str of dna."""

def bin2dna(msg_encoded):
    output = ''
    translator = {'0':'C', '1':'T'}
    for char in msg_encoded:
        output += translator[char]
    new_output = []
    new_output.append(output[0])
    for letter in output[1:]:
        if letter == new_output[-1]:
            if letter == 'C':
                new_output.append('A')
            elif letter == 'A':
                new_output.append('C')
            elif letter == 'T':
                new_output.append('G')
            else:
                new_output.append('T')
        else:
            new_output.append(letter)
    output = ''
    for char in new_output:
        output += char
    return output 



"""this function translate from dna to bin code
param_1: str of dna (came out from the sequencer or from 4) not seperated
return: str of binar code, with or without code against mistakes in it."""

def dna2bin(msg):
    output = ''
    dict = {'A':'0', 'C':'0', 'G':'1', 'T':'1'}
    for char in msg:
        output += dict[char]
    return output