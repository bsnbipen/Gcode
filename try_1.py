import numpy as np
import re
x="G01 Z 0.431 F$global[7]" 
dict_axes={"X":[],"Y":[],"Z":[]}


def convert_dictpara(param,pump_info): 
    default_dict={"X":0,"Y":0,"Z":0}
    num=1
    info_list=[] 
    line_list=x.split()                          #convertes the splited lines into a dictionary with axis
    for i,lines in enumerate(line_list):
        if (re.search(r"[A-Z]+\$[a-z]+\D[0-8]+\D",lines)):
            del line_list[i]
    for i,lines in enumerate(line_list):
        if (re.search(r"[A-Z][0-1][0-1]",lines)):
            del line_list[i]
            break
    #print (line_list)
    axis=["X","Y","Z"]
    value_dct={v:line_list[(i+1)] for i,v in enumerate(line_list) if v=="X" or v=="Y" or v=="Z"}
    #print (value_dct)
    for keys in value_dct.keys():
        default_dict[keys]=value_dct[keys]
    info_list.append(num)
    info_list.append(pump_info)
    for axes in axis:
        info_list.append(default_dict[axes])
    info_array=np.array(info_list)
    print(info_array)
    #print(default_dict)
    return default_dict
    
"""
def exclude_f(take_dict):
   for i,v in enumerate(take_dict):
        if (re.search(r"\F\$(global)\[\d\]",v) or:
            del take_dict[i]
   return take_dict
"""
a=convert_dictpara(x,"On")

#print(a)