#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: printer_5
# Project: DNA-Storage-alpha
# Author: Zohar baron
# Email: zoharbaron2002@gmail.com
# Created: 03/07/19 14:05
"""this function will multiply the mols and then add mistakes to them.
parameter_1: list of strings already transleted to DNA and and divided to oligos.
parameter_2: a = int, num of the times the printer multiply each oligo.
param_3: b = int, from 0-b is the chance that there will be a mistake un a specific char (each specific char).
param_4: c = int, under c is the % for delition mistake
param_5: d = int, between c to d is the % for .
return: str """

import math
import random


def printer_dna(dna_list, a, b, c, d):
    #oligos_list = [dna_list[5*i:5*i+10] for i in range(int(math.ceil(len(dna_list)/5)))]
    #
    oligos_list = ''
    for char in dna_list:
        oligos_list += char
    #
    multiple_oligos = []
    #for oligo in oligos_list:
    multiple_oligos.append([oligos_list for i in range(a)])
    printed_oligos = []
    molecule = ''
    for oligo in multiple_oligos:
        for mol in oligo:
            for char in mol:
                mistake_chance = random.random()
                if mistake_chance > b :
                    molecule += char
                else:
                    mistake_type = random.randrange(0, 100)
                    if mistake_type < c:
                        continue
                    elif mistake_type > c and mistake_type < d:
                        chars_list = ['A', 'T', 'C', 'G']
                        random_char = random.choice(chars_list)
                        molecule += char
                        molecule += random_char
                    else:
                        chars_list = ['A', 'T', 'C', 'G']
                        random_char = random.choice(chars_list)
                        while random_char == char:
                            random_char = random.choice(chars_list)
                        molecule += random_char
            printed_oligos.append(molecule)
            molecule = ''
    return printed_oligos

a = 10
b = 0.1#
c = 33
d = 66

