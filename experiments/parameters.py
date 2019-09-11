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
from experiments import mistakes
#import matplotlib.pyplot as plt

def big_main_function():
    my_data = pd.DataFrame(columns = ['a_value', 'b_value','c_value','d_value','g_valu','h_vlue','k_value','j_value','r_value'])
    function_list = [function_1, function_2, function_3, function_4, function_5, function_6]
    for function in function_list: 
        a_values = [50, 100, 200]
        k_values = [10, 50, 100]
        r_values = [3, 5, 9]
        b_values = [0.001, 0.01, 0.1]
        for a in a_values:
            for k in k_values:
                for r in r_values:
                    for b in b_values:
                        #save data frame_to file
                        _ = """writer = pd.ExcelWriter('myDataFrame.xlsx')
                        my_dataframe.to_excel(writer, 'DataFrame')
                        writer.save()"""
                        with open('C:\\Users\\user\\Desktop\\zohar\\Alpha\\Study\\DNA-Storage-alpha\\experiments\\results_pandas.xlsx', 'w') as f:
                            f.write(str(my_data))
                        params = [a, b, 10, 20, 10, 20, k, 100,r]
                        for t in range(10):
                            print("runing function {}".format(function.__name__))
                            output = params.append(function.main(*params))
                            array_output = pd.array(output)
                            #update data_frame
                            my_data.append(array_output, ignore_index = True)
                            print(params, output)

big_main_function()