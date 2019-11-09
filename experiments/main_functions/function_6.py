#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: function_3
# Project: DNA-Storage-alpha
# Author: Leon Anavy and Zohar Baron
# Email: anavy (at) technion (dot) ac (dot) il
# Created: 01/07/2019 14:28
import sys 
sys.path.append('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha')
from experiments import input
from encoding.bin2dna import one_bit_3B
from encoding.dna_coding import repeatition_code_4A
from simualtors.synthesizers import pre_print
from simualtors.synthesizers import printer_5
from simualtors.sequencers import NGS_7A
from experiments import mistakes
import time

def main(a,b,c,d,g,h,k,j,r):
    msg_in = input.create_input(j)
    dna = one_bit_3B.bin2dna(msg_in)
    dna_encoded = repeatition_code_4A.encode(dna,r)
    dna_seperate = pre_print.pre_print(dna_encoded, k)
    dna_mol_syn = printer_5.printer_dna(dna_seperate, a, b, c, d)
    reads = NGS_7A.dna_sequencer(dna_mol_syn, b, g, h, a, k)
    reads_one_str = NGS_7A.api_sequencer(reads, dna_seperate[1], dna_seperate[2],a, dna_seperate[3])
    msg_decoded = repeatition_code_4A.decode(reads_one_str,r)
    msg_read = one_bit_3B.dna2bin(msg_decoded)
    mistakes_presentage = mistakes.mistake_presentage(msg_in, msg_read)
    num_of_oligos_generaly = len(dna_seperate[0]) * a
    num_of_nukleotides_generaly = num_of_oligos_generaly * dna_seperate[1]
    end = time.time()
    time_it_takes = end - start
    return [mistakes_presentage, time_it_takes, len(dna_encoded), len(dna_seperate[0]), dna_seperate[1], num_of_oligos_generaly, num_of_nukleotides_generaly]