# Topic: behavior of view-buttons

import cadquery as cq

if 'show_object' not in globals():
    def show_object(self, name, options={}, **kwargs):
        return
    
if 'debug' not in globals():    
    def debug(self, obj, args={}):
        return

part = cq.Workplane("XY").box(30,30,30)

part = part.faces("<Z").workplane(centerOption="CenterOfMass").text("bottom",5,-1)  # bottom
part = part.faces(">Z").workplane(centerOption="CenterOfMass").text("top",5,-1)     # top
part = part.faces("<X").workplane(centerOption="CenterOfMass").text("left",5,-1)    # left
part = part.faces(">X").workplane(centerOption="CenterOfMass").text("right",5,-1)   # right
part = part.faces("<Y").workplane(centerOption="CenterOfMass").text("back",5,-1)    # back
part = part.faces(">Y").workplane(centerOption="CenterOfMass").text("front",5,-1)   # front

bottom = part.faces("<Z")
top    = part.faces(">Z")
left   = part.faces("<X")
right  = part.faces(">X")
back   = part.faces("<Y")
front  = part.faces(">Y")

show_object(part,name="part",options={"alpha":0.0,"color":(255,170,0)})

debug(front,name="front")

# Behavior:
# Iso    (Shift+F2): back-top-right   !!! no front !!!
# Top    (Shift F3): top
# Bottom (Shift F4): bottom           !!! upside-down !!!
# Front  (Shift F5): front
# Back   (Shift F6): back
# Left   (Shift F7): left
# Right  (Shift F8): right