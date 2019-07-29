#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: printer_5
# Project: DNA-Storage-alpha
# Author: Zohar baron
# Email: zoharbaron2002@gmail.com
# Created: 11/07/19 12:33

"""this function devide the str of already encoded DNA to oligonukleotides and add to them indexes.
param_1: str of dna encoded came from 3 or 4
param_2: k: len of each oligonukleotide
return: list of str in it, each str is a oligo(/mol)"""

import math

def pre_print(dna_str, k):
    oligos_list = []
    oligos_list_no_index = [dna_str[int(k//2)*i:int(k//2)*i+k] for i in range(int(math.ceil(len(dna_str)/int(k//2))))]
    oligos_list_no_index = oligos_list_no_index[:-1]
    print(oligos_list_no_index)
    x = 0
    for i, oligo in enumerate(oligos_list_no_index):
        while len(oligo) != k:
            oligo += 'A'
            x += 1
        with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\add_zeros.txt', 'w') as f:
            f.write(f"pre_print added {x} times 'A' to oligonukleotide number {i}. /n")
        print(i, oligo)
        index_1 = bin(i)[2:]
        print(index_1)
        if len(index_1) % 2 != 0:
            index_1 = '0' + index_1
            with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\add_zeros.txt', 'w') as f:
                f.write(f"pre_print added '0' to index number {i} /n")
        index_2 =  " "
        index_divided = [index_1[2*z:2*z+2] for z in range(int(math.ceil(len(index_1)/2)))]
        print(index_divided)
        indexes_list = []
        for pair in index_divided:
            translator = {'01': 'T', '10': 'A', '00': 'G', '11': 'C'}
            index_2 += translator[pair]
        oligo_1 = index_2 + oligo
        print(index_2)
        print(oligo_1)
            indexes_list.append(index_2)
    lenght = len(indexes_list[-1])
    for i, oligo in enumerate(oligos_list_no_index):
        #while len(index_2) < lenght:
            #index_2 += A 
        #לעשות רשימה של כל האינדקסים, לבדוק מה הארוך של האינדקס האחרון ולהוסיך לכל שאר האינדקסים לפי אותו מספר (לא צריך לכתוב את זה נראה לי) ואז להוסיף כל אינדקס לאוליגו שלו
        print(oligo_1)
        oligos_list.append(oligo_1)
        print(oligos_list)
        new_list = []
        for tuple_ in oligos_list:
            tuple_ = tuple_[0] + tuple_[1]
            str(tuple_)
            new_list.append(tuple_)
    print(new_list)
    return new_list, lenght


#
k = 6
dna_str = 'ACGTACGTACGTACGT'
pre_print(dna_str, k)
#