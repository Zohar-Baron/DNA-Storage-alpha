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
    msg_len = max(len(msg_in), len(msg_decoded))
    correct_num = 0
    for i, (char_1, char_2) in enumerate(zip(msg_in, msg_decoded)):
        if char_1 == char_2:
            correct_num += 1
    #print(msg_in, msg_decoded, correct_num, msg_len)
    mistake_present = 100-(correct_num/msg_len)*100
    return mistake_present

def average(mistake_presentage_list):
    sum = mistake_presentage_list[0] + mistake_presentage_list[1] + mistake_presentage_list[2] + mistake_presentage_list[3] + mistake_presentage_list[4] + mistake_presentage_list[5] + mistake_presentage_list[6] + mistake_presentage_list[7] + mistake_presentage_list[8] + mistake_presentage_list[9]
    divide_by = len(mistake_presentage_list)
    average = sum/divide_by
    return average