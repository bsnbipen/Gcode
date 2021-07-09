# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:37:38 2021

@author: bipen
"""

import pandas as pd
import re

default_value_dict={"X":0,"Y":0,"Z":0,"E":0}
X_axis=[]
Y_axis=[]
Z_axis=[]
E_axis=[]
values_dict={"X":X_axis,"Y":Y_axis,"Z":Z_axis,"E":E_axis}
line="G1 X48.471 Y53.557 E5.09205"
line_list=line.split()

def game_of_number(another_dict):
    print(another_dict)
    for keys in another_dict.keys():
        default_value_dict[keys]=another_dict[keys]
    axis=["X","Y","Z","E"]
    for axis_name in axis:
        values_dict[axis_name].append(default_value_dict[axis_name])
        
        


def exclude_f(take_dict):
   for i in list(take_dict):
        if i=="F":
            del take_dict[i]
   return take_dict

def convert_dictpara(param):
    exam_dct={param[num][0]:param[num][1:] for num in range(0, len(param))}
    return_dict=exclude_f(exam_dct)
    return return_dict

def take_gcode(location):
    with open(location,'r') as reader:
        for line in reader:
            if (re.search(r"G",line)):
                line=line.split()
                line=convert_dictpara(line)
                game_of_number(line)
                
                    
#Your location here
take_gcode(r"C:\Users\bb237\Desktop\Conformal\e_extruder\g_code_box.txt")


df=pd.DataFrame(values_dict,columns=["X","Y","Z","E"])                   
df.to_csv(r'C:\Users\bb237\Desktop\Conformal\e_extruder\axis_coordinate.csv',index=False)