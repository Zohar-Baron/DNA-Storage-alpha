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

from experiments.main_functions import function_1
from experiments.main_functions import function_2
from experiments.main_functions import function_3
from experiments.main_functions import function_4
from experiments.main_functions import function_5
from experiments.main_functions import function_6
from experiments.main_functions import function_7
from experiments.main_functions import function_8
from experiments import mistakes
#import matplotlib.pyplot as plt

def most_main_function():
    function_list = [function_1, function_2, function_3, function_4, function_5, function_6, function_7, function_8]
    for function in function_list: 
        t = 0
        a_values_list = []
        k_values_list = []
        #חזרה
        ave_mistakes_list = []
        while t != 10:
            value_1 = {a:4, b:0.001, c:33, d:66, e:33, f:66, g:33, h:66, k:4}
            parametres_list = [a, b, c, d, e, f , g, h, k]
            for param in parameters_list:
                param = value_1[param]
            main(a, b, c, d, e, f, e , g, h, k)
            if t == 9:
               ave_mistakes = mistakes.average(mistake_presentage_list)#לעשות ממוצע
               ave_mistakes_list.append(ave_mistakes)
            t += 1 
        while t > 9 and t < 20:
            value_2 = {a:8, b:0.01, c:33, d:66, e:33, f:66, g:33, h:66, k:6}
            parametres_list = [a, b, c, d, e, f, e , g, h, k]
            for param in parameters_list:
                param = value_2[param]
            main(a, b, c, d, e, f, e , g, h, k)
            t += 1
        while t > 19 and t < 30:
            value_3 = {a:10, b:0.05, c:33, d:66 , e:33, f:66, g:33, h:66, k:10}
            parametres_list = [a, b, c, d, e, f, e , g, h, k]
            for param in parameters_list:
                param = value_3[param]
            main(a, b, c, d, e, f, e , g, h, k)
            t += 1
        while t > 29 and t < 40:
            value_4 = {a:20, b:0.1 , c:33 , d:66, e:33, f:66, g:33, h:66, k:20}
            parametres_list = [a, b, c, d, e, f, e , g, h, k]
            for param in parameters_list:
                param = value_4[param]
            main(a, b, c, d, e, f, e , g, h, k)
            t += 1
        while t > 39 and t < 50:
            value_5 = {a:50, b:0.3, c:33, d:66, e:33, f:66, g:33, h:66, k:50}
            parametres_list = [a, b, c, d, e, f, e , g, h, k]
            for param in parameters_list:
                param = value_5[param]
            main(a, b, c, d, e, f, e , g, h, k)
            t += 1
        plt.plot([x], [ave_mistakes_list]) #לעשות גרף מכל הנקודות וואי שנשמרו לאורך הדרך


def big_main_function():
    function_list = [function_1]#, function_2, function_3, function_4, function_5, function_6]
    for function in function_list: 
        a_values = [10, 50, 100]
        k_values = [10, 50, 100]
        r_values = [3, 5, 9]
        b_values = [0.01, 0.1, 0.5]
        for a in a_values:
            for k in k_values:
                for r in r_values:
                    for b in b_values:
                        params = [a, b, 33, 66, 33,66, 33, 66, k, 100]
                        for t in range(10):
                            print("runing function {}".format(function.__name__))
                            output = function.main(*params)
                            print(params, output)

big_main_function()