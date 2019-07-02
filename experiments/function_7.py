#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: function_1
# Project: DNA-Storage-alpha
# Author: Leon Anavy and Zohar Baron
# Email: anavy (at) technion (dot) ac (dot) il
# Created: 01/07/2019 14:32

from encoding.bin2dna.two_bits import two_bits_3
from encoding.dna_coding import something_code_4B
from simualtors.synthesizers import printer_5
from simualtors.storage import storage_6
from simualtors.sequencers import NGS_7A
from encoding.reads2seq import dna2bin_9

def main():
    print('generate message')
    msg_in = '01010110'
    print('convert to dna')
    dna_encoded = two_bits_3.bin2dna(msg_in)
    print('encode message')
    msg_encoded = something_code_4B.encode(dna_encoded)
    print('synthesize dna')
    dna_mol_syn = printer_5.print_dna(msg_encoded)
    print('store dna')
    dna_mol_stor = storage_6.store(dna_mol_syn)
    print('sequence dna')
    reads = NGS_7A.dna_sequence(dna_mol_stor)
    print('infer dna sequence')
    dna_seq_read = dna2bin_9.infer(reads)
    print('convert to binary')
    msg_read = two_bits_3.dna2bin(dna_seq_read)
    print('decode message')
    msg_decoded = something_code_4B.decode(msg_read)
    print('done:')
    print(msg_in,msg_decoded)

if __name__ == '__main__':
	main()