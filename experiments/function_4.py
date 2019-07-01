#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: function_2
# Project: DNA-Storage-alpha
# Author: Leon Anavy and Zohar Baron
# Email: anavy (at) technion (dot) ac (dot) il
# Created: 01/07/2019 14:17

from encoding.bin_coding import heming_code_2B
from encoding.bin2dna.two_bits import two_bits_3
from simualtors.synthesizers import printer_5
from simualtors.storage import storage_6
from simualtors.sequencers import nanopore_7B
from encoding.reads2seq import dna2bin_9

def main():
    print('generate message')
    msg_in = '01010110'
    print('encode message')
    msg_encoded = heming_code_2B.encode(msg_in)
    print('convert to dna')
    dna_encoded = two_bits_3.bin2dna(msg_encoded)
    print('synthesize dna')
    dna_mol_syn = printer_5.print_dna(dna_encoded)
    print('store dna')
    dna_mol_stor = storage_6.store(dna_mol_syn)
    print('sequence dna')
    reads = nanopore_7B.dna_sequence(dna_mol_stor)
    print('infer dna sequence')
    dna_seq_read = dna2bin_9.infer(reads)
    print('convert to binary')
    msg_read = two_bits_3.dna2bin(dna_seq_read)
    print('decode message')
    msg_decoded = heming_code_2B.decode(msg_read)
    print('done:')
    print(msg_in,msg_decoded)

if __name__ == '__main__':
	main()