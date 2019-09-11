#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: printer_5
# Project: DNA-Storage-alpha
# Author: Zohar baron
# Email: zoharbaron2002@gmail.com
# Created: 03/07/19 14:05
"""this function will multiply the mols and then add mistakes to them.
parameter_1: list of strings already transleted to DNA and divided to oligos. came from pre_print.
parameter_2: a = int, the num of the times the printer multiply each oligo.
param_3: b = int, from 0-b is the chance that there will be a mistake in a specific char (each specific char).
param_4: c = int, under c is the % for delition mistake
param_5: d = int, between c to d is the % for .
return: list of moleculs (str) in it. """

import math
import random


def printer_dna(oligos_list, a, b, c, d):
    #print(oligos_list)
    multiple_oligos = []
    #print(multiple_oligos)
    for oligo in oligos_list[:-3]:
        multiple_oligos.append([oligo for i in range(a)])
    #print(multiple_oligos)
    printed_oligos = []
    molecule = ''
    for big_list in multiple_oligos:
        for list_oligo in big_list:
            for oligo in list_oligo:
                for char in oligo:
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
    #print(printed_oligos)
    return printed_oligos

#printer_dna(['ACGT','CGTA','GTAC','TACG'],4, 0.1,33,66)




def printer_dna_2(oligos_list, a, c, d):
    """כתלות בסוג בסיס"""
    multiple_oligos = []
    for oligo in oligos_list:#
        for i in range(a):
            multiple_oligos.append(oligo)#
    print(multiple_oligos)
    printed_oligos = []
    molecule = ''
    for mol in multiple_oligos:
        for char in mol:###
            mistake_chance = random.random()
            if char == 'A':
                if mistake_chance > 0.02 :
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
            elif char == 'C':
                if mistake_chance > 0.04 :
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
            elif char == 'G':
                if mistake_chance > 0.06 :
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
            else:
                if mistake_chance > 0.08 :
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
    print(printed_oligos)
    return printed_oligos

#printer_dna_2(['ACGT','CGTA','GTAC','TACG'],4,33,66)

def printer_dna_3(oligos_list ,a,b,c,d):
    """כתלות בהומופולימר"""
    multiple_oligos = []
    for oligo in oligos_list:#
        for i in range(a):
            multiple_oligos.append(oligo)#
    print(multiple_oligos)
    printed_oligos = []
    molecule = ''
    for mol in multiple_oligos:
        for i, char in enumerate(mol):###
            mistake_chance = random.random()
            if multiple_oligos[i] == multiple_oligos[i-1]:
                if mistake_chance > 0.5 :
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
            else: 
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
    print(printed_oligos)
    return printed_oligos


#printer_dna_3(['ACGT','CGTA','GTAC','TACG'],4,0.1,33,66)

def printer_dna_4(oligos_list, a, b, c, d):
    #כתלות בטעויות קודמות
    multiple_oligos = []
    for oligo in oligos_list:
        for i in range(a):
            multiple_oligos.append(oligo)
    print(multiple_oligos)
    printed_oligos = []
    molecule = ''
    for oligo in multiple_oligos:
        molecule += oligo[0]
        for i, char in enumerate(oligo[1:]):
            mistake_chance = random.random()
            if molecule[i-1] != oligo[i-1]:
                if mistake_chance > 0.5 :
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
            else:
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
    print(printed_oligos)
    return printed_oligos

#printer_dna_4(['ACGT','CGTA','GTAC','TACG'],4, 0.1,33,66)


def printer_dna_5(oligos_list, a, c, d):
    #with all the options
    #לזכור להוסיף את החלק של ההכפלה בהתחלה
    b_values_by_letter = {'A': 0.1, 'G':0.15, 'C':0.2,'T':0.09}
    for oligo in oligos_list:
        temporary_list = []
        temporary_list.append(oligo[0])
        for i ,char in enumerate(oligo):
            mistake_chance = random.random()
            b = 0
            b += b_values_by_letter[char]

            if char == temporary_list[-1]:
                b += 0.03
            if oligo[i-1] != temporary_list[-1]:
                b += 0.07


            


printer_dna_5(['ACGT','CGTA','GTAC','TACG'],0.1,33,66)