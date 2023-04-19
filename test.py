import cadquery as cq
from cadquery import exporters

outer   = cq.Workplane("XY").box(440,140,2)                                  # outer
inner   = cq.Workplane("XY").box(420,120,4)                                  # inner
cutout2 = cq.Workplane("XY").box(85,20,6).translate((-0.5*(420-85)-6,0,0))   # cutout2
cutout1 = cq.Workplane("XY").box(85,18,6).translate((-0.5*(420-85)-5,0,0))   # cutout1

result = outer.cut(inner).cut(cutout2)
result = result.union(cutout1)
result = result.section(0)

#debug(outer)
#debug(inner)
#debug(cutout2)
#debug(cutout1)
show_object(result,name="result",options={"alpha":0.2,"color":(255,170,0)})

exporters.export(result, "test.dxf")