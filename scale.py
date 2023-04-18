# HowTo: scale a CQ-object, looking for the counterpart of OpenSCAD scale([x,y,z])

import cadquery as cq

#result = cq.Workplane().box(100,100,100).scale(0.1)            # same factor for all axis

# or 

#result = cq.Workplane().box(100,100,100).scale((0.2,0.1,0.5))  # individual factor for each axis

big   = cq.Workplane().box(100,100,100)
small = big.val().scale(0.1).translate((75,0,0))

show_object(big,name="big",options={"alpha":0.2,"color":(255,170,0)})
show_object(small,name="small",options={"alpha":0.2,"color":(255,170,0)})