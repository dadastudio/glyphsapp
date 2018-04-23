#MenuTitle: Bind anchors with a node at distance
# -*- coding: utf-8 -*-
__doc__="""
Bind anchors with a node at distance
"""

import GlyphsApp
import math

Font = Glyphs.font

# Glyphs.clearLog()
# Glyphs.showMacroWindow()

angle=math.radians(Font.selectedFontMaster.italicAngle)

def getPt(p1,p2):

  if p1 > p2.position.y:
    target=-p1+p2.position.y
  else:
    target=p2.position.y-p1
  return target

selection = Font.selectedLayers[0].selection

firstPoint=selection[0]

if isinstance (firstPoint,GSNode):

  firstPoint.userData["distAnchors"]=list()

  for selectedPoint in  selection:

    if selectedPoint!=firstPoint: 

      if isinstance (selectedPoint,GSAnchor):

        
        yTarget=getPt(firstPoint.y,selectedPoint)

        selectedPoint.x= firstPoint.x + yTarget * math.tan( angle ) 

        firstPoint.userData["distAnchors"].append(selectedPoint.name) 
else:
  print "ERROR: First point of a selection must be a node!"
