# HowTo: taper

import cadquery as cq

part = cq.Workplane("XY").box(30,30,30).faces(">Z").workplane()
part = part.rect(20,20).extrude(-20,combine='s',taper=15)
