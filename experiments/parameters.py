#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
# Licensed under the MIT License.
# Filename: parameters
# Project: DNA-Storage-alpha
# Author: Zohar Baron
# Email: ZoharBaron2002@gmail.com
# Created: 08/07/2019 10:53

"""this file will tel to the main function ("function_1"/..._2...)
in wich values use for each parameters each time it run"""
import pandas as pd
from experiments.main_functions import function_1
from experiments.main_functions import function_2
from experiments.main_functions import function_3
from experiments.main_functions import function_4
from experiments.main_functions import function_5
from experiments.main_functions import function_6
#from experiments.main_functions import function_9
#from experiments.main_functions import function_10
from experiments import mistakes

def big_main_function():
    function_list = [function_1, function_2, function_3, function_4, function_5, function_6]#, function_9, function10]
    j_values = [100, 1000]
    k_values = [25, 150]
    r_values = [3, 9, 21, 33]
    b_values = [0.00001, 0.0001, 0.001, 0.01, 0.1]
    my_data = pd.DataFrame(columns = ['a_value', 'b_value','c_value','d_value','g_valu','h_vlue','k_value','j_value','r_value','mistakes_presentage', 'time_it_takes', 'len_dna_encoded', 'num_of_different_oligos', 'oligo_nukleotides_full_length', 'num_of_oligos_generaly', 'num_of_nukleotides_generaly', 'repetition_num', 'which_function'], index = range(2 * len(a_values) * len(b_values) * len(k_values) * len(r_values) * len(function_list)))
    line = 1
    for function in function_list: 
        for j in j_values:
            for k in k_values:
                for r in r_values:
                    for b in b_values:
                        params = [50, b, 10, 20, 10, 20, k, j, r] 
                        for t in range(20):
                            print("runing function {}".format(function.__name__))
                            output = function.main(*params)
                            function_name = "{}".format(function.__name__)
                            print(params, output)
                            my_data.loc[line] = pd.Series({'a_value': a, 'b_value': b ,'c_value': 10,'d_value': 20,'g_valu':10,'h_vlue':20 ,'k_value':k,'j_value': 100,'r_value':r,'mistakes_presentage':output[0], 'time_it_takes':output[1], 'len_dna_encoded':output[2], 'num_of_different_oligos':output[3], 'oligo_nukleotides_full_length':output[4], 'num_of_oligos_generaly':output[5], 'num_of_nukleotides_generaly':output[6], 'repetition_num':t, 'which_function':function_name})
                            line += 1
                            my_data.to_csv('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\results\________.csv')

big_main_function()