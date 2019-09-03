#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: printer_5
# Project: DNA-Storage-alpha
# Author: Zohar baron
# Email: zoharbaron2002@gmail.com
# Created: 11/07/19 12:33

"""this function devides the str of already encoded DNA to oligonukleotides and adds indexes to them.
param_1: str of dna encoded came from 3 or 4
param_2: k: len of each oligonukleotide
return: list of str in it, each str is a oligo(/mol)"""

import math

def pre_print(dna_str, k):
    oligos_list = []
    oligos_list_no_index = [dna_str[int(k//2)*i:int(k//2)*i+k] for i in range(int(math.ceil(len(dna_str)/int(k//2))))]
    oligos_list_no_index = oligos_list_no_index[:-1]
    x = 0
    oligos_new_list = []
    for i, oligo in enumerate(oligos_list_no_index):
        while len(oligo) != k:
            oligo += 'A'
            x += 1
        oligos_new_list.append(oligo)
    with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\add_zeros.txt', 'a') as f:
        f.write(f"""pre_print added {x} times 'A' to oligonukleotide number {i}. 
        """)
    indexes_list_1 = []
    for i, oligo in enumerate(oligos_new_list):
        index_1 = bin(i+1)[2:]
        indexes_list_1.append(index_1)
    max_len = len(indexes_list_1[-1])
    if max_len % 2 != 0:
        indexes_list_1[-1] = '0' + indexes_list_1[-1]
    max_len = len(indexes_list_1[-1])
    with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\add_zeros.txt', 'a') as f:
        f.write(f"""index length = {max_len}.
        """)
    indexes_list = []
    index_divided_list = [] 
    for index in indexes_list_1:
        index_len = len(index)
        while index_len != max_len:
            index = '0' + index
            index_len = len(index)
        encoded_index = ""
        for char in index:
            encoded_index += 3 * char
        indexes_list.append(encoded_index)   ##?   
        index_divided_list.append([encoded_index[2*z:2*z+2] for z in range(int(math.ceil(len(encoded_index)/2)))])
    indexes_translated = []
    for index_divided in index_divided_list:
        index_2 = ''
        for pair in index_divided:
            translator = {'01': 'T', '10': 'A', '00': 'G', '11': 'C'}
            index_2 += translator[pair]
        indexes_translated.append(index_2)
    for oligo, index in zip(oligos_new_list, indexes_translated):
        oligo_1 = index + oligo
        full_length = len(oligo_1)
        oligos_list.append(oligo_1)
    index_len = len(indexes_translated[-1])
    #print(oligos_list, index_len, full_length)
    return oligos_list, full_length, index_len
   


#
#k = 6
#dna_str = 'ACGTACGTACGTACGT'
#pre_print(dna_str, k)
#