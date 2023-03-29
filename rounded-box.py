# HowTo: rounded box

import cadquery as cq

result = (
   cq.Sketch()
   .box(100, 100, 100)
   .edges()
   .fillet(10)
)

# show_object(result,name="result",options={"alpha":0.2,"color":(255,170,0)})