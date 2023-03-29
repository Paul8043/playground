# HowTo: rounded rectangle

import cadquery as cq

result = (
   cq.Sketch()
   .rect(100, 100)
   .vertices()
   .fillet(10)
)

# show_object(result,name="result",options={"alpha":0.2,"color":(255,170,0)})