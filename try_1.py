import numpy as np
import warnings 
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)





from scipy.spatial import distance
from scipy.spatial import distance
import re
import math
x="G01 Z 0.431 F$global[7]" 

constant_print={"layer_height":0.3, 
"f_layer_height":0.4, 
"def_layer_width":0.5,
"rad_filament":3.7, 
"nozzle_dia":0.5, 
}


dict_axes={"X":[],"Y":[],"Z":[]}




info_array=np.array([1,0,[(0,0,0)]],dtype=object,ndmin=2)
#print("At the start:",info_array)



def calculation(info_coord):
    area_road=(((constant_print["def_layer_width"]-constant_print["layer_height"])*constant_print["layer_height"])+(math.pi*math.pow(constant_print["layer_height"]/2,2)))
    fil_area=math.pi*math.pow(constant_print["rad_filament"],2)
    dist_trav=distance.cdist(info_array[-1][-1],info_coord[-1],'euclidean')
    extrusion=round(float((area_road*dist_trav)/(fil_area)),5)
    print("The extrusion is:",extrusion)

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
    value_dct={v:line_list[(i+1)] for i,v in enumerate(line_list) if v=="X" or v=="Y" or v=="Z"}        #creates a dictionary with X,Y and Z values
    #print (value_dct)
    
    for keys in value_dct.keys():
        default_dict[keys]=value_dct[keys]                                                              #keeps the default values in the dictionary
    
    info_axes=[tuple(float(default_dict[axes]) for axes in axis)]                                       #creates a list of tuple coordinates
 
    
    
    info_list.append(num)
    info_list.append(pump_info)
    info_list.append(info_axes)
    #print(info_list)
    calculation(info_list)
    temp_array=np.vstack((info_array,info_list))
    #print(temp_array)
    return temp_array
    
"""
def exclude_f(take_dict):
   for i,v in enumerate(take_dict):
        if (re.search(r"\F\$(global)\[\d\]",v) or:
            del take_dict[i]
   return take_dict
"""
info_array=convert_dictpara(x,1)

#print(info_array)

