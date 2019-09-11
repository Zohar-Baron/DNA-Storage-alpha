#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: printer_5
# Project: DNA-Storage-alpha
# Author: Zohar baron
# Email: zoharbaron2002@gmail.com
# Created: 03/07/19 15:09
"""this function add mistakes, and then select just the mols with the write len (and correct also a bit of the mistakes in them?)
param: list of str in it came from 6
return:one str of DNA"""
import math
import random


def dna_sequencer(stored_data, b, g, h, a, k):
    #print(dna_sequencer)#
    sequenced_dna = []
    molecule = ''
    for mol in stored_data:
        for char in mol:
            mistake_chance = random.random()
            if mistake_chance > b :
                molecule += char
            else:
                mistake_type = random.randrange(0, 100)
                if mistake_type < g:
                    continue
                elif mistake_type > g and mistake_type < h:
                    chars_list = ['A', 'T', 'C', 'G']
                    random_char = random.choice(chars_list)
                    molecule += random_char
                else:
                    chars_list = ['A', 'T', 'C', 'G']
                    random_char = random.choice(chars_list)
                    while random_char == char:
                        random_char = random.choice(chars_list)
                    molecule += char
                    molecule += random_char
        sequenced_dna.append(molecule)
        molecule = ''
    #יוצרת רשימה ובתוכה רשימות של חצאי אוליגונוקלאוטידם שזהים אחד לשני (לפי האינדקס)
	#משווה ביניהם ואם יש משהו ממש יוצא דופן אז מוחקת אותו לגמרי
    #משווה בין כל תו ברשימה (הראשונה) ואם הוא שווה לאותו התו ברוב שאר הרשימות של אותו אוליגונוקלאוטיד, אז מוסיפה אותו לרשימה החדשה שתהיהי האאוטפוט
    return sequenced_dna
### מה עומק הריצוף???

"""this function is...
param_1: sequenced_dna: list of strings each one is an oligonukleotide and exists several times
full_length : the length of each oligonukleotide inclod the index
index_len : the length of each index
return: one str of dna"""

import math
def api_sequencer(sequenced_dna, full_length, index_len, a, num_of_A_added):
    #print(len(sequenced_dna))
    sequenced_dna = [oligo for oligo in sequenced_dna if len(oligo) == full_length]
    #print(len(sequenced_dna))
    num_of_different_oligos = len(sequenced_dna)//a
    list_of_lists = [[] for i in range(num_of_different_oligos)]
    output = ''
    translator2= {'T': '01', 'A': '10', 'G': '00', 'C': '11'}
    i = 0
    for oligo in sequenced_dna:
        index = oligo[:index_len]
        #print(index)
        output = ''
        for letter in index:
            output += translator2[letter]
        #print(output)
        groups_of_3_list = [output[3*i:3*i+3] for i in range(int(math.ceil(len(output)/3)))]
        #print(groups_of_3_list)
        original_msg = ''
        for group in groups_of_3_list:
            sum = int(group[0]) + int(group[1]) + int(group[2])
            if sum >1:
                original_msg += '1'
            else:
                original_msg += '0' 
        original_msg = original_msg.lstrip('0')
        #print(original_msg)       
        try:
            oligo_place = int(original_msg, 2)-1
        except:
            #print("failed to cinvert to binary")
            continue
        #print(oligo_place)
        try:
            list_of_lists[oligo_place].append(oligo[index_len:full_length])
        except:
            pass
    #print(list_of_lists)
    new_list_of_lists = [[]for i in range (len(list_of_lists)+1)]
    i = 0
    for same_oligo_list in list_of_lists:
        for oligo in same_oligo_list:
            huff_oligo = int(len(oligo)/2)
            new_list_of_lists[i].append(oligo[:huff_oligo]) 
            new_list_of_lists[i+1].append(oligo[huff_oligo:])
        i += 1
    letter_to_place = {'A':0, 'C':1, 'G':2, 'T':3}
    place_to_letter = {0:'A', 1:'C', 2:'G', 3:'T'}
    final_output = ''
    for same_oligos in new_list_of_lists:
        if len(same_oligos) == 0:
            continue
        ammount_of_oligos = len(same_oligos)
        for i in range(len(same_oligos[0])):
            bases_num = [0, 0, 0, 0]
            for oligo in same_oligos:
                bases_num[letter_to_place[oligo[i]]] += 1
            largest_base = max(bases_num)
            largest_base_place = bases_num.index(largest_base)
            final_output += place_to_letter[largest_base_place] 
    #print(final_output)
    if num_of_A_added != 0:
        final_output = final_output[:-num_of_A_added]
    return final_output


#api_sequencer(['GGGTATGAGTAGACC', 'GTCGTGTGACATGCA', 'GTCGTGTGACATGCA', 'GTCGTGTGACATGCA','GTCGTGTGACATAGG', 'GGGTATGAGTAGACC', 'GGGTATGAGTAGACC', 'CGTACAGTACTCGAT'], 16, 3, 4)