import cadquery as cq

outer  = cq.Workplane("XY").box(440,140,2)                                  # outer
inner  = cq.Workplane("XY").box(420,120,2)                                  # inner
cutout = cq.Workplane("XY").box(85,18,4).translate((-0.5*(420-85)-5,0,0))   # cutout

result = outer.cut(inner)
show_object(result,name="result",options={"alpha":0.2,"color":(255,170,0)})
