#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: function_1
# Project: DNA-Storage-alpha
# Author: Leon Anavy
# Email: anavy (at) technion (dot) ac (dot) il
# Created: 01/07/2019 03:37
import sys 
sys.path.append('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha')
from experiments import input
from encoding.bin_coding import repeatition_code_2A
from encoding.bin2dna.two_bits import two_bits_3
from simualtors.synthesizers import pre_print
from simualtors.synthesizers import printer_5
from simualtors.storage import storage_6
from simualtors.sequencers import NGS_7A
from experiments import mistakes

def main(a,b,c,d,e,f,g,h,k, j):
    print('generate message')
    msg_in = input.create_input(j)###
    print('encode message')
    msg_encoded = repeatition_code_2A.encode(msg_in)
    print('convert to dna')
    dna_encoded = two_bits_3.bin2dna(msg_encoded)
    print('seperate dna')
    dna_seperate = pre_print.pre_print(dna_encoded, k)
    print('synthesize dna')
    dna_mol_syn = printer_5.printer_dna(dna_seperate, a, b, c, d)
    print('store dna')
    dna_mol_stor = storage_6.store_dna(dna_mol_syn, e, f, b)
    print('sequence dna')
    reads = NGS_7A.dna_sequencer(dna_mol_stor, b, g, h, a, k)
    reads_one_str = NGS_7A.api_sequencer(reads, dna_seperate[1], dna_seperate[2],a)
    print('infer dna sequence')
    msg_read = two_bits_3.dna2bin(reads_one_str)
    print('convert to binary')
    msg_decoded = repeatition_code_2A.decode(msg_read)
    mistakes_presentage = mistakes.mistake_presentage(msg_in, msg_decoded)
    mistake_presentage_list = []
    mistake_presentage_list.append(mistakes_presentage)
    with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\results.txt', 'w') as f:
        f.write(f"input: {msg_in}   output: {msg_decoded}    mistakes_presentage: {mistakes_presentage} % /n" )
    print('mistake presentage' , mistakes_presentage)
    print('done:')
    return mistakes_presentage_list


#a = 12
#b = 0
#c = 25
#d = 50
#e = 25
#f = 50
#g = 25
#h = 50
#k = 6
#j = 50

#if __name__ == '__main__':
#	main(a,b,c,d,e,f,g,h,k)
