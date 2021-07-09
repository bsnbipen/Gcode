import re
from try_1 import coord_pump_off

def output_line(file_location):





init_stat_=["G92 E0","G92 E0","G1 Z0.300 F1200.000","G1 E-2.00000 F2400.00000","G92 E0"]    # This call should be written once at the top only
init_stat=["G1 E2.00000 F2400.00000","G1 F600"]                                             # Frequently called calls
with open (r"C:\Users\bb237\Desktop\G-Code_Examples\output.txt",'a') as file:
        file.seek(0) 
        file.truncate()
        for stat in init_stat:
            file.write(stat)
        with open (r"C:\Users\bb237\Desktop\G-Code_Examples\Gcode_try_conformal(1).txt",'r') as reader:
            for line_value in reader:                    
                    #line_list=line.split()
                    if (re.search(r"\$\D\w\[\d\]\.\X\=",line_value)):                   #check here
                        line_value=line_value.split()
                        pump_status=line_value[0][-1]

                    elif (int(pump_status)is 1):                                        #for pump on
                                              line_list=line_value.split()
                        if re.search('^[G]01', line_list[0]):
                            info_gcode=coord_pump_on(line_value,pump_status)
                            for i,lines in enumerate(line_list):
                            if (re.search(r"[A-Z]+\$[a-z]+\D[0-8]+\D",lines)):
                                del line_list[i]
                                for i,lines in enumerate(line_list):
                            if (re.search(r"[A-Z][0-1][0-1]",lines)):
                                del line_list[i]
                                break
                            axis=["X","Y","Z"]
                            value_dct={v:line_list[(i+1)] for i,v in enumerate(line_list) if v=="X" or v=="Y" or v=="Z"}  
                            output=line_list[0]+" ".join(v+str(value_dct[v]) for v in value_dct.keys)+ " E" + info_gcode[-1]
                            file.write(output)
                            
                    elif (int(pump_status) is 0):
                        line_list=line_value.split()
                        if re.search('^[G]01', line_list[0]):
                            info_gcode=coord_pump_off(line_value,pump_status)
                            for i,lines in enumerate(line_list):
                            if (re.search(r"[A-Z]+\$[a-z]+\D[0-8]+\D",lines)):
                                del line_list[i]
                                for i,lines in enumerate(line_list):
                            if (re.search(r"[A-Z][0-1][0-1]",lines)):
                                del line_list[i]
                                break
                            axis=["X","Y","Z"]
                            value_dct={v:line_list[(i+1)] for i,v in enumerate(line_list) if v=="X" or v=="Y" or v=="Z"}  
                            output=line_list[0]+" ".join(v+str(value_dct[v]) for v in value_dct.keys)+ " E"
                            file.write(output)
'''                         

                    if re.search('^[G]01', line_list[0]]):
                            for i,lines in enumerate(line_list):
                            if (re.search(r"[A-Z]+\$[a-z]+\D[0-8]+\D",lines)):
                                del line_list[i]
                                for i,lines in enumerate(line_list):
                            if (re.search(r"[A-Z][0-1][0-1]",lines)):
                                del line_list[i]
                                break
                            axis=["X","Y","Z"]
                            value_dct={v:line_list[(i+1)] for i,v in enumerate(line_list) if v=="X" or v=="Y" or v=="Z"}  
                            output=line_list[0]+" ".join(v+str(value_dct[v]) for v in value_dct.keys)
                                
                            `