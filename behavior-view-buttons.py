# Topic: behavior of view-buttons

import cadquery as cq

if 'show_object' not in globals():
    def show_object(self, name, options={}, **kwargs):
        return
    
if 'debug' not in globals():    
    def debug(self, obj, args={}):
        return

part = cq.Workplane("XY").box(20,20,20)

part = part.faces("<Z").workplane(centerOption="CenterOfMass").text("-Z",5,-1)
part = part.faces(">Z").workplane(centerOption="CenterOfMass").text("+Z",5,-1)
part = part.faces("<X").workplane(centerOption="CenterOfMass").text("-X",5,-1)
part = part.faces(">X").workplane(centerOption="CenterOfMass").text("+X",5,-1)
part = part.faces("<Y").workplane(centerOption="CenterOfMass").text("-Y",5,-1)
part = part.faces(">Y").workplane(centerOption="CenterOfMass").text("+Y",5,-1)

bottom = part.faces("<Z")
top    = part.faces(">Z")
left   = part.faces("<X")
right  = part.faces(">X")
front  = part.faces("<Y")
back   = part.faces(">Y")

show_object(part,name="part",options={"alpha":0.0,"color":(255,170,0)})

#debug(bottom,name="bottom")
#debug(top,name="top")
#debug(left,name="left")
#debug(right,name="right")
debug(front,name="front")
#debug(back,name="back")

#rotated = bottom.rotate([0,0,0],[0,0,1],180)
#show_object(rotated,name="rotated",options={"alpha":0.0,"color":(0,128,0)})

# Behavior:
# Top    (Shift F3): +Z
# Bottom (Shift F4): Z-  !!! upside-down !!!
# Front  (Shift F5): +Y  !!! back !!!
# Back   (Shift F6): -Y  !!! front !!!
# Left   (Shift F7): -X
# Right  (Shift F8): +X