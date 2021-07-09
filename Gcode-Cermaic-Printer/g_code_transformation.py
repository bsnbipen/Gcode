# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 11:21:23 2021

@author: bb237
"""
"""
Constants
$global[1]=0.1 
$global[2]=0.2 
$global[3]=0 
$global[4]=0 
$global[5]=0.1 
$global[6]=0.2 
$global[7]=15 
$global[8]=20 

"""
import re
import math
import numpy as np

radian=math.radians(180)
axis_name=["X","Y","Z"]
trans_mat_z=np.array([[1,0,0],
             [0,math.cos(radian),-math.sin(radian)],
             [0,math.sin(radian),math.cos(radian)]])

mirror_about_z=np.array([[-1,0,0],
             [0,1,0],
             [0,0,1]])

constant_1={"$global[1]":0.1, 
"$global[2]":0.2, 
"$global[3]":0,
"$global[4]":0,
"$global[5]":0.1, 
"$global[6]":0.2, 
"$global[7]":(15/4)*60,
"$global[8]":(20/4)*60,
}


def rotate_about_x_axis(taken_list):
    axis_in_line=set("XYZ")&set(taken_list)
    if axis_in_line:
        a=dict(X=0,Y=0,Z=0)
        for k,v in enumerate(taken_list):
            for axis in axis_in_line:
                if v== axis:
                    a[axis]=taken_list[k+1]
        coord=np.array([float(a["X"]),
                float(a["Y"]),
                float(a["Z"])])
        rotate_along_z_axis=np.matmul(trans_mat_z,coord)
        dict_coor={name:rotate_along_z_axis[i] for i,name in enumerate(axis_name)}\
    
        for k,v in enumerate(taken_list):
            for axis in axis_in_line:
                if v== axis:
                    taken_list[k+1]=str(dict_coor[v])
                    # print(taken_list)
        return taken_list
    else:
        return taken_list
    
def mirror_function(taken_list):
    axis_in_line=set("XYZ")&set(taken_list)
    if axis_in_line:
        a=dict(X=0,Y=0,Z=0)
        for k,v in enumerate(taken_list):
            for axis in axis_in_line:
                if v== axis:
                    a[axis]=taken_list[k+1]
        coord=np.array([float(a["X"]),
                float(a["Y"]),
                float(a["Z"])])
        rotate_along_z_axis=np.matmul(mirror_about_z,coord)
        dict_coor={name:rotate_along_z_axis[i] for i,name in enumerate(axis_name)}\
    
        for k,v in enumerate(taken_list):
            for axis in axis_in_line:
                if v== axis:
                    taken_list[k+1]=str(dict_coor[v])
                    # print(taken_list)
        return taken_list
    else:
        return taken_list
    
def translation_matrix(taken_list):
    translate_about_z=np.array([[1,0,0,0],
             [0,1,0,0],
             [0,0,1,29.68],
             [0,0,0,1]])
    axis_in_line=set("XYZ")&set(taken_list)
    if axis_in_line:
        a=dict(X=0,Y=0,Z=0)
        for k,v in enumerate(taken_list):
            for axis in axis_in_line:
                if v== axis:
                    a[axis]=taken_list[k+1]
        coord=np.array([float(a["X"]),
                float(a["Y"]),
                float(a["Z"]),
                1])
        rotate_along_z_axis=np.matmul(translate_about_z,coord)
        print(rotate_along_z_axis)
        dict_coor={name:rotate_along_z_axis[i] for i,name in enumerate(axis_name)}\
    
        for k,v in enumerate(taken_list):
            for axis in axis_in_line:
                if v== axis:
                    taken_list[k+1]=str(round(dict_coor[v],3))
                    # print(taken_list)
        return taken_list
    else:
        return taken_list

# line="G01   X 19.005   Y 72.740   Z -2.018 F$global[8]"
# lines=line.split()
# for i,linesx in enumerate(lines):
#     if (re.search(r"[A-Z]+\$[a-z]+\D[0-8]+\D",linesx)):
#        for keys in constant_1.keys():
#            # print(keys)
#            if keys==linesx[1:]:
#                lines[i]=constant_1[keys]
#                # print(lines[i])

with open (r"C:\Users\bb237\Desktop\G-Code_Examples\output.txt",'a') as file:
        file.seek(0)
        file.truncate()
        with open (r"C:\Users\bb237\Desktop\G-Code_Examples\Gcode_try_conformal(1).txt",'r') as reader:
            for line in reader:
                if (re.search('^G', line)):
                    line_list=line.split()
                    # print(line_list)
                    # line_list=mirror_function(line_list)
                    
                    # print(type(line_list))
                    for i,lines in enumerate(line_list):
                         if (re.search(r"[A-Z]+\$[a-z]+\D[0-8]+\D",lines)):
                           for keys in constant_1.keys():
                               # print(keys)
                               if keys==lines[1:]:
                                   line_list[i]=lines[0]+str(constant_1[keys])
                                   output_line=" ".join(str(elements) for elements in line_list)+"\n"
                                   file.write(output_line)
                            

