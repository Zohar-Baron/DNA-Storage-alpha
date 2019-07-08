#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: printer_5
# Project: DNA-Storage-alpha
# Author: Zohar baron
# Email: zoharbaron2002@gmail.com
# Created: 03/07/19 14:48
"""this function will simulate storage time. it will add mistakes randomly (how mach we will say).
it will change the str to list (probably) and at the end changed it back. 
parameter_1: str (from the printer)
type: str
return: str (parameter_1 + mistakes. maybe also the oligos mixed?)""" 



import math
import random


def store_dna(printed_oligos, e, f, b):
    stored_data = []
    molecule = ''
    for mol in printed_oligos:
        for char in mol:
            mistake_chance = random.random()
            if mistake_chance > b :
                molecule += char
            else:
                mistake_type = random.randrange(0, 100)
                if mistake_type < e:
                    continue
                elif mistake_type > e and mistake_type < f:
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
        stored_data.append(molecule)
        molecule = ''
    return stored_data

b = 0.1#
e = 33
f = 66

