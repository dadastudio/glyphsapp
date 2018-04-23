#MenuTitle: Bind  anchors with a selected node 
# -*- coding: utf-8 -*-
__doc__="""
Bind anchors with a node in a font. 
"""

import GlyphsApp
import vanilla
Font = Glyphs.font

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

selection=Font.selectedLayers[0].selection
firstPoint=selection[0]

if isinstance (firstPoint,GSNode):

  firstPoint.userData["anchors"]=list()

  for selectedPoint in  selection:

    if selectedPoint!=firstPoint: 

      if isinstance (selectedPoint,GSAnchor):
        selectedPoint.x= firstPoint.x 
        selectedPoint.y= firstPoint.y 

        firstPoint.userData["anchors"].append(selectedPoint.name)
      else:
        print "This is not an anchor"
else:
  print "First point must be a GSNode instance" 



