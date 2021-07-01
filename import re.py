import re
import pandas as pd

constant_1={"$global[1]":0.1, 
"$global[2]":0.2, 
"$global[3]":0,
"$global[4]":0,
"$global[5]":0.1, 
"$global[6]":0.2, 
"$global[7]":(15/4)*60,
"$global[8]":(20/4)*60,
}

default_value_dict={"X":0,"Y":0,"Z":0,"E":0}
X_axis=[]
Y_axis=[]
Z_axis=[]
E_axis=[]
values_dict={"X":X_axis,"Y":Y_axis,"Z":Z_axis,"E":E_axis}
line="G1 X48.471 Y53.557 E5.09205"
status="off"                                #default status of pump

"""
G01   Z 0.431 F$global[7] 
G01   Z 0.431 F$global[7] 
G01   X 19.808   Y 60.876 
G01   Z 3.478 
"""


def axis(another_dict,status):
    if status=="off"
        print("G01 %")
        
        print()
    print(another_dict)
    for keys in another_dict.keys():
        default_value_dict[keys]=another_dict[keys]
    axis=["X","Y","Z","E"]
    for axis_name in axis:
        values_dict[axis_name].append(default_value_dict[axis_name])

def pump_status(line):
    if line[-1]==0:
        status="off"
    else
        status=="on"



def gcode_define(line):


def take_conformal_code(line_value):                    #takes the location of the file
    #with open(location,'r') as reader:
        #for line in reader:
            if (re.search(r"\$\D\w\[\d\]\.\X\=",line_value)):                   #check here
                pump_status(line_value)
            
                line_value=line_value.split()
                line_value=convert_dictpara(line)
                axis(line_value,status)


def convert_dictpara(param):                            #convertes the splited lines into a dictionary with axis
    exam_dct={param[num][0]:param[num][1:] for num in range(0, len(param))}
    return_dict=exclude_f(exam_dct)
    return return_dict