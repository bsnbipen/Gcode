import numpy as np
import warnings
from numpy.lib.utils import info 
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)





from scipy.spatial import distance
from scipy.spatial import distance
import re
import math


constant_print={"layer_height":0.3, 
"f_layer_height":0.4, 
"def_layer_width":0.6,
"rad_filament":3.8, 
"nozzle_dia":0.5, 
}

constant_speed={
"pump_off":(15/4)*60,
"pump_on":(20/4)*60,
}

dict_axes={"X":[],"Y":[],"Z":[]}


starting_point=(43.699,36.246,-42.695)                                           #the starting point for the print---    >Change For each Print<----


list_extrusion=[2]
pump_status=0
info_tuple=[[str(0),[(0,0,0)],0],[str(0),[starting_point],0]]              #second element of this list is the starting point for the print
default_dict={"X":0,"Y":0,"Z":0}




def calculation(info_coord):
    global list_extrusion,info_tuple
    area_road=(((constant_print["def_layer_width"]-constant_print["layer_height"])*constant_print["layer_height"])+(math.pi*math.pow(constant_print["layer_height"]/2,2)))
    fil_area=math.pi*math.pow(constant_print["rad_filament"],2)
    

    dist_trav=distance.cdist(info_tuple[-1][-2],info_coord[-1],'euclidean')
    extrusion=(float((area_road*dist_trav)/(fil_area)))
    list_extrusion.append(extrusion)
    sum_extrusion_array=np.sum(list_extrusion)

    return round(sum_extrusion_array,5)

def coord_pump_off(param,pump_info):
    global info_tuple,default_dict  
    num=1
    info_list=[] 
    line_list=param.split()                          #convertes the splited lines into a dictionary with axis
    for i,lines in enumerate(line_list):
        if (re.search(r"[A-Z]+\$[a-z]+\D[0-8]+\D",lines)):
            del line_list[i]
    for i,lines in enumerate(line_list):
        if (re.search(r"[A-Z][0-1][0-1]",lines)):
            del line_list[i]
            break

    
    axis=["X","Y","Z"]
    value_dct={v:line_list[(i+1)] for i,v in enumerate(line_list) if v=="X" or v=="Y" or v=="Z"}        #creates a dictionary with X,Y and Z values

    
    for keys in value_dct.keys():
        default_dict[keys]=value_dct[keys]                                                              #keeps the default values in the dictionary
    
    info_axes=[tuple(float(default_dict[axes]) for axes in axis)]
    

    info_list.append(pump_info)
    info_list.append(info_axes)                                       #creates a list of tuple coordinates
    info_list.append(0)
    info_tuple.append(info_list)
    return info_tuple

def coord_pump_on(param,pump_info): 
    global info_tuple,default_dict

    num=1
    info_list=[] 
    line_list=param.split()                          #convertes the splited lines into a dictionary with axis
    for i,lines in enumerate(line_list):
        if (re.search(r"[A-Z]+\$[a-z]+\D[0-8]+\D",lines)):
            del line_list[i]
    for i,lines in enumerate(line_list):
        if (re.search(r"[A-Z][0-1][0-1]",lines)):
            del line_list[i]
            break

    
    axis=["X","Y","Z"]
    value_dct={v:line_list[(i+1)] for i,v in enumerate(line_list) if v=="X" or v=="Y" or v=="Z"}        #creates a dictionary with X,Y and Z values

    
    for keys in value_dct.keys():
        default_dict[keys]=value_dct[keys]                                                              #keeps the default values in the dictionary
    
    info_axes=[tuple(float(default_dict[axes]) for axes in axis)]                                       #creates a list of tuple coordinates
 
    

    info_list.append(pump_info)
    info_list.append(info_axes)

    val_e=calculation(info_list)
    info_list.append(val_e)

    info_tuple.append(info_list)

    return info_tuple
    


def output_line(input_file_location,output_file_location):
    init_stat_1=["G92 E0","G92 E0","G1 Z0.300 F1200.000","G1 E-2.00000 F2400.00000","G92 E0"]    # This call should be written once at the top only
    init_stat_2=["G1 E2.00000 F2400.00000"+"\n","G1 F600"]
    init_speed=[" F"+ str(constant_speed["pump_off"])+"\n","G01"+" F"+ str(constant_speed["pump_on"])+"\n"]                                             # Frequently called calls
    global pump_status
    with open (output_file_location,'a') as file:
        file.seek(0) 
        file.truncate()

        with open (input_file_location,'r') as reader:
            for stat in init_stat_1:
                file.write(stat+"\n")
            for i,line_value in enumerate(reader):                    
                    line_list=line_value.split()
                    if (re.search(r"\$\D\w\[\d\]\.[A-Z]\=",line_list[0])):                   #check here
                        print(line_list)
                        pump_status=line_list[0][-1]
                        



                    elif (line_list[0]=="G01"):

                        if (int(pump_status)== 1):
                            if(i==3):
                                file.write(init_stat_2[0])
                            info_gcode=coord_pump_on(line_value,pump_status)
                            axis=["X","Y","Z"]
                            value_dct={v:line_list[(i+1)] for i,v in enumerate(line_list) if v=="X" or v=="Y" or v=="Z"}  
                        
                            if(info_tuple[-2][0]==str(0)):
                         
                                output="G01"+" "+" ".join(v+str(value_dct[v]) for v in ["X","Y"])+ init_speed[0]
                                file.write(output)
                                output="G01"+" "+"Z"+value_dct["Z"]+ init_speed[0]
                                file.write(output)
                                file.write(init_speed[1])
                            else:
                                output="G01"+" "+" ".join(v+str(value_dct[v]) for v in value_dct)+ " E" + str(info_gcode[-1][-1])+"\n"
                                file.write(output)
                            
                        elif (int(pump_status) == 0):

                            info_gcode=coord_pump_off(line_value,pump_status)
                            axis=["X","Y","Z"]
                            value_dct={v:line_list[(i+1)] for i,v in enumerate(line_list) if v=="X" or v=="Y" or v=="Z"}  
                            
   
                            if(info_tuple[-2][0]== str(1)):
                         
                                output="G01"+" "+" ".join(v+str(value_dct[v]) for v in value_dct)+"\n"
                                file.write(output)
            




output_line(r"C:\Users\bb237\Gcode\Output Example\conformal_for_print.txt",r"C:\Users\bb237\Gcode\Output Example\output.txt")        #input file location,output file location
        #change the output file location



