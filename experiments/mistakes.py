#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: repeatition_code
# Project: DNA-Storage-alpha
# Author: Zohar Baron
# Email: zoharbaron2002@gmail.com
# Created: 08/07/2019 15:46
"""this function will    """

def mistake_presentage(msg_in, msg_decoded):
    msg_len = len(msg_in)
    mistake_num = 0
    i = 0
    for char_1, char_2 in zip(msg_in, msg_decoded):
        if char_1 != char_2:
            mistake_num += 1
        i += 1
    mistake_present = (mistake_num/msg_len)*100
    return mistake_present
