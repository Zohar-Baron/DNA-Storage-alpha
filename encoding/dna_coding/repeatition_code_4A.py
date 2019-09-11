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

def encode(msg, r):
    #print(msg)
    out_msg = ''
    for char in msg:
        out_msg += r * char
    return out_msg


"""this function do the oposite from the one above, 
it takes a str of DNA and returns it without the multiple characters an without mistakes (hopfully)
param: str of DNA came out from the sequencer
return: str of shorter DNA"""
def decode(word,r):
    groups_list = [word[r*i:r*i+r] for i in range(int(math.ceil(len(word)/r)))]
    #print(groups_list)
    original_msg = ''
    letter_to_place = {'A':0, 'C':1, 'G':2, 'T':3}
    place_to_letter = {0:'A', 1:'C', 2:'G', 3:'T'}
    for group in groups_list:
        bases_num = [0, 0, 0, 0]
        for char in group:
            base_place = letter_to_place[char]
            bases_num[base_place] += 1
            #print(bases_num)
        largest_base = max(bases_num)
        largest_base_place = bases_num.index(largest_base)
        right_base = place_to_letter[largest_base_place]
        original_msg += right_base
    #print(original_msg)
    return original_msg

#decode('AAACCCGGGTTT', 3)



def encode_chanks(word, r):
    groups_of_3_list = [word[3*i:3*i+3] for i in range(int(math.ceil(len(word)/3)))]
    #if its not dividing to 3...
    out_word = ''
    for group in groups_of_3_list:
        out_word += r*group
    #print(out_word)
    return out_word

#encode_chanks('ACGTGCATAGCGCTA', 3)


def decoded_chanks(msg, r):
    groups_list = [msg[3*r*i:3*r*i+3*r] for i in range(int(math.ceil(len(msg)/(3*r))))]
    letter_to_place = {'A':0, 'C':1, 'G':2, 'T':3}
    place_to_letter = {0:'A', 1:'C', 2:'G', 3:'T'}
    output = ''
    for group in groups_list:
        for i in range(3):  
            bases_num = [0,0,0,0]
            for j in range(r):
                base_place = letter_to_place[group[i + 3*j]]
                bases_num[base_place] += 1
            largest_base = max(bases_num)
            largest_base_place = bases_num.index(largest_base)
            right_base = place_to_letter[largest_base_place]
            output += right_base
    #print(output)
    return output



#decoded_chanks('ACGACGACGTGCTGCTGCATAATAATACGCCGCCGCCTACTACTA', 3)
