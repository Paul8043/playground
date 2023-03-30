# HowTo: stacked extrusions

import cadquery as cq

locations = [(-35,0),(0,0),(35,0)]

part = cq.Workplane("XY").box(100,30,30).faces(">Z").workplane()
part = part.pushPoints(locations)
part = part.rect(20,20).extrude(-5,combine='s')
part = part.pushPoints(locations)
part = part.rect(10,10).extrude(-10,combine='s')