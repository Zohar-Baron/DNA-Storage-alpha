#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: function_2
# Project: DNA-Storage-alpha
# Author: Leon Anavy and Zohar Baron
# Email: anavy (at) technion (dot) ac (dot) il
# Created: 01/07/2019 14:17
import sys 
sys.path.append('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha')
from experiments import input
from encoding.bin_coding import hamming_code_2B
from encoding.bin2dna import one_bit_3B
from simualtors.synthesizers import pre_print
from simualtors.synthesizers import printer_5
from simualtors.sequencers import NGS_7A
from experiments import mistakes
import time

def main(a,b,c,d,g,h,k,j,r):
    start = time.time()
    #print('generate message')
    msg_in = input.create_input(j)
    #print('encode message')
    msg_encoded = hamming_code_2B.encode(msg_in)
    #print('convert to dna')
    dna_encoded = one_bit_3B.bin2dna(msg_encoded[0])
    #print('seperate dna')
    dna_seperate = pre_print.pre_print(dna_encoded, k)
    #print('synthesize dna')
    dna_mol_syn = printer_5.printer_dna(dna_seperate, a, b, c, d)
    #print('sequence dna')
    reads = NGS_7A.dna_sequencer(dna_mol_syn,b, g, h, a, k)
    reads_one_str = NGS_7A.api_sequencer(reads, dna_seperate[1], dna_seperate[2],a, dna_seperate[3])
    #print('infer dna sequence')
    msg_read = one_bit_3B.dna2bin(reads_one_str) # here is the "מצקת"
    #print('convert to binary')
    msg_decoded = hamming_code_2B.decode(msg_read, msg_encoded[1])
    mistakes_presentage = mistakes.mistake_presentage(msg_in, msg_decoded)
    #print('mistake presentage' , mistakes_presentage)
    #print('done:')
    num_of_oligos_generaly = len(dna_seperate[0]) * a
    num_of_nukleotides_generaly = num_of_oligos_generaly * dna_seperate[1]
    end = time.time()
    time_it_takes = end - start
    return [mistakes_presentage, time_it_takes, len(dna_encoded), len(dna_seperate[0]), dna_seperate[1], num_of_oligos_generaly, num_of_nukleotides_generaly]