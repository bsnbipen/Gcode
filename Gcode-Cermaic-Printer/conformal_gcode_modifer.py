# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:40:06 2021

@author: bb237
"""
import re
pump_status={"$DO[8].X=1":1, 
"$DO[8].Y=1":1, 
"$DO[8].Z=1":1,
"$DO[8].X=0":0,
"$DO[8].Y=0":0, 
"$DO[8].Z=0":0, 
}



status=0
counter=0
with open (r"C:\Users\bb237\Desktop\G-Code_Examples\output.txt",'a') as file:
        file.seek(0)
        file.truncate()
        with open (r"C:\Users\bb237\Desktop\G-Code_Examples\Gcode_try_conformal(1).txt",'r') as reader:
            for line in reader:
                # if (re.search('^G', line)):
                    line_list=line.split()
                    # print(line_list)
                    # line_list=mirror_function(line_list)
                    
                    # print(type(line_list))
                    for i,lines in enumerate(line_list):
                         if (re.search(r"^\$([A-Z])\w\[\d\]\.\w\=\d",lines)):
                             counter+=1
                             for keys in pump_status.keys():
                               # print(keys)
                               if keys==lines:
                                   
                                   status+=pump_status[keys]
                                   line_list[i]=lines[0]+str(pump_status[keys])
                                   output_line=" ".join(str(elements) for elements in line_list)+"\n"
                                   file.write(output_line)