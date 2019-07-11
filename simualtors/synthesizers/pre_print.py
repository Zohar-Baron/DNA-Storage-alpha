#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: printer_5
# Project: DNA-Storage-alpha
# Author: Zohar baron
# Email: zoharbaron2002@gmail.com
# Created: 11/07/19 12:33

"""this function devide the str of akredy encoded DNA to oligonukleotides and add to them indexes.
param_1: str of dna encoded came from 3 or 4
param_2: a: len of each oligonukleotide
return: list of str in it, each str is a oligo(/mol)"""

import math

def pre_print(dna_str, a):
    oligos_list = []
    oligonukleotide_2 = ''
    oligos_list_no_index = [dna_str[int(a//2)*i:int(a//2)*i+a] for i in range(int(math.ceil(len(dna_str)/int(a//2))))]
    print(oligos_list_no_index)
    x = 0
    while len(oligos_list_no_index[-1]) != a:
        oligos_list_no_index[-1] += 'A'
        x += 1
        with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\add_zeros.txt', 'w') as f:
            f.write(f"pre_print added {x} times 'A' to last oligonukleotide. /n")
    for i, oligonukleotide_1 in enumerate(oligos_list_no_index):
        index_1 = bin(i)[2:]
        print(index_1)
        if len(index_1) % 2 != 0:
            index_1 += '0'
            with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\add_zeros.txt', 'w') as f:
            f.write(f"pre_print added '0' to index number {i} /n")
        index_2 = ''
        index_divided = [index_1[2*i:2*i+2] for i in range(int(math.ceil(len(index_1)/2)))]
        for pair in index_divided:
            translator = {'01': 'T', '10': 'A', '00': 'G', '11': 'C'}
            index_2 += translator[pair]
        for oligo in oligos_list_no_index:
            oligonukleotide_2 += index_2 
            oligonukleotide_2 += oligonukleotide_1
        oligos_list.append(oligonukleotide_2)
        oligonugleotide_2 = ''
    print(oligos_list)
    return oligos_list

a = 6
dna_str = 'ACGTACGTACGTACGT'
pre_print(dna_str, a)