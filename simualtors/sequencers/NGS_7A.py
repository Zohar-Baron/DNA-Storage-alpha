#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: printer_5
# Project: DNA-Storage-alpha
# Author: Zohar baron
# Email: zoharbaron2002@gmail.com
# Created: 03/07/19 15:09
"""this function    """
import math
import random


def dna_sequencer(stored_data, b, g, h):
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

