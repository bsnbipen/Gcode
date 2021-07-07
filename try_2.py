from scipy.spatial import distance
import numpy as np
import math
list_1=[(1,0,0)]
list_2=[(0,1,0)]
dm=distance.cdist(list_1,list_2,'euclidean')
#$print(dm)




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