#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: printer_5
# Project: DNA-Storage-alpha
# Author: Zohar baron
# Email: zoharbaron2002@gmail.com
# Created: 03/07/19 15:09
"""this function add mistakes, and then select just the mols woth the write len (and correct also a bit of the mistakes in them?)
param: list of str in it came from 6
return:one str of DNA"""
import math
import random


def dna_sequencer(stored_data, b, g, h, a, k):
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
    for molecule in sequenced_dna:
        if len(molecule) != k:
            sequenced_dna.remove(molecule)
    #יוצרת רשימה ובתוכה רשימות של חצאי אוליגונוקלאוטידם שזהים אחד לשני (לפי האינדקס)
	#משווה ביניהם ואם יש משהו ממש יוצא דופן אז מוחקת אותו לגמרי
    #משווה בין כל תו ברשימה (הראשונה) ואם הוא שווה לאותו התו ברוב שאר הרשימות של אותו אוליגונוקלאוטיד, אז מוסיפה אותו לרשימה החדשה שתהיהי האאוטפוט
    return sequenced_dna


"""this function is...
param_1: sequenced_dna: list of strings each one is an oligonukleotide and exists several times
return: one str of dna"""

def api_sequencer(sequenced_dna, k, lenght):
    indexs_list = []
    indexes_list.append(sequenced_dna[0][0:lenght + 1])
    for molecule in sequenced_dna:
        if len(molecule) != k:
            sequenced_dna.remove(molecule)
    for molecole in sequenced_dna[0:]:
        if molecule[0:lenght+1] == indexs_list[-1]:
            indexes_list.append(molecole[0:lenght + 1])
