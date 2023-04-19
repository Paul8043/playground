# HowTo: export 2D-objects as DXF

"""
This is a question that belongs to my original issue #1282 (#1277 and #487 are touching
similiar topics)

Task: The 3 rectangles below should go as 2D-objects into a single SVG-file and the
      dimensions should be preserved (no re-scaling allowed).

I have learned that the current exporters.export(result, "file.svg") cannot do this
at the moment. Because of this I am considering to write an additional exporter that
makes a few things easier.

You have recommended for CAD-applications, I should use DXF instead of SVG. I have
reached the stage where I can make this experiment. I am trying this, as a primlinary
work-a-round. The idea is: export the rectangles to a DXF-file. And hopefully
FreeCAD or QCAD can convert this to an un-scaled SVG-file.

Questions:

1. Why are rectangles red, they should be a yellow-tone?

2. How to glue the rectangles together?
a) Put all 3 rectangles into a single Workplane. Seems the last wins! How to put rectangles,
   that might have individual translations, into each other? 
b) I have tried to make unions, but this seems to work only with 3D-objects.
c) I have tried to put them into an assembly. That works, but I am not
   able to get the colors right. And more severe, exportDXF expects
   Workplane-objects and not assemblies.

I am curious to see what you will propose! How is the way out?
"""

import cadquery as cq

outer  = cq.Workplane("XY").rect(440,140)                                  # outer
inner  = cq.Workplane("XY").rect(420,120)                                  # inner
cutout = cq.Workplane("XY").rect(85,18).translate((-0.5*(420-85)-5,0,0))   # cutout

all    = cq.Workplane("XY").rect(440,140).rect(420,120).rect(85,27).translate((-0.5*(420-85)-2.5,0,0))  # last wins
#show_object(all,name="all",options={"alpha":0.2,"color":(255,170,0)})

#show_object(outer,name="outer",options={"alpha":0.2,"color":(255,170,0)})
#show_object(inner,name="inner",options={"alpha":0.2,"color":(255,170,0)})
#show_object(cutout,name="cutout",options={"alpha":0.2,"color":(255,170,0)})

# idea from last night
s1 = cq.Sketch().rect(440,140).edges()
s2 = cq.Sketch().rect(420,120).edges()
s3 = cq.Sketch().rect(85,18).edges()
wp =cq.Workplane("XY").placeSketch(s1,s2,s3)
#show_object(wp,name="wp",options={"alpha":0.2,"color":(255,170,0)})    # does not show anything