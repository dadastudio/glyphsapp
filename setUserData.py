#MenuTitle: Set User Data
# -*- coding: utf-8 -*-
__doc__="""
Sets user data
"""
import uuid

import GlyphsApp
import vanilla
import math
Font = Glyphs.font
verticalStems=Font.selectedFontMaster.verticalStems
angle=Font.selectedFontMaster.italicAngle
Glyphs.clearLog()
Glyphs.showMacroWindow()

selectedLayer = Font.selectedLayers[0]
selection = selectedLayer.selection

component= selection[0]
node= selection[1]

# node.userData["component"]=component
# node= selection[0]

uidk=uuid.uuid1()

component.anchor=str(uidk)
node.userData["components"]=[component.anchor]

for c in node.userData["components"]:
  for comp in selectedLayer.components:
    if comp.anchor==c:
      ref=0
      for anch in comp.component.layers[0].anchors:
        if anch.name =="origin":
          ref=anch.x
          print ref
      
      comp.transform = ((
                        1, # x scale factor
                        0.0, # x skew factor
                        0.0, # y skew factor
                        1, # y scale factor
                        node.position.x-ref, # x position
                        node.position.y  # y position
                        ))
  
#   c.position=node.position



# selectedLayer.components[node.userData['component']]


# for selected in  selection:


  # print selectedPoint.userData
  # selectedPoint.userData["node"]={"type":"stemLeft"}
  # selectedPoint.userData["node"]={"y":690,"type":"extend"}
