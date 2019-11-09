#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: repeatition_code
# Project: DNA-Storage-alpha
# Author: Zohar Baron
# Email: zoharbaron2002@gmail (dot) com
# Created: 20/08/2019 12:42

""" this function will write (randomly) the input each
param: j: the len of the output of this function.
return: str of zeros and ones"""

import random
def create_input(j):
    msg_in = ''
    msg_in_len = len(msg_in)
    while msg_in_len != j:
        which_num = random.random()
        if which_num < 0.5:
            msg_in += '0'
        else: 
            msg_in += '1'
        msg_in_len = len(msg_in)
    return msg_in