# HowTo: stacked extrusions (same as stacked-extrusions, but with rounded pockets)

import cadquery as cq

locations = [(-35,0),(0,0),(35,0)]
s1 = cq.Sketch().rect(20,20).vertices().fillet(3)   # large shape
s2 = cq.Sketch().rect(15,15).vertices().fillet(3)   # small shape

part = cq.Workplane("XY").box(100,30,30).faces(">Z").workplane()
part = part.pushPoints(locations)
part = part.placeSketch(s1).extrude(-10,combine='s')
part = part.pushPoints(locations)
part = part.placeSketch(s2).extrude(-20,combine='s')