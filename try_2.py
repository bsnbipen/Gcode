from scipy.spatial import distance
import numpy as np
import math
list_1=[(1,0,0)]
list_2=[(0,1,0)]
dm=distance.cdist(list_1,list_2,'euclidean')
info_extrusion=np.array([2])

x="G01   X 19.808   Y 60.876   Z 3.478 F$global[8]"
list_3=x.split()

print(list_3)

#$print(dm)
'''dict_axes={"X":0,"Y":0,"Z":0}
line="    $DO[8].X=1 "
axis=["X","Y","Z"]

list=["a","b",axis]

output="AB "+" ".join(v+str(dict_axes[v]) for v in dict_axes)

print(output)

#output=line_list[0]+" ".join(v+str(value_dct[v]) for v in value_dct.keys)+"\n"
#line_value=line.split()
#print(int(line_value[0][-1]) is 1)
"""
constant_print={"layer_height":0.3, 
"f_layer_height":0.4, 
"def_layer_width":0.5,
"rad_filament":3.7, 
"nozzle_dia":0.5, 
}
#print(math.pi*math.pow(constant_print["layer_height"]/2,2))
#print(constant_print["def_layer_width"])

#area_road=(((constant_print["def_layer_width"]-constant_print["layer_height"])*constant_print["layer_height"])+(math.pi*math.pow(constant_print["layer_height"]/2,2)))
fil_area=math.pi*math.pow(constant_print["rad_filament"],2)

print (fil_area)
'''