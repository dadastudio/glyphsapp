#MenuTitle: Move anchors to their nodes
# -*- coding: utf-8 -*-
__doc__="""
Move anchors to their nodes
"""

import GlyphsApp
import vanilla
import math
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()
angle=float(Font.selectedFontMaster.italicAngle)

def getItalic(x, y, angle ):
  return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )

def getPt(p1,p2):

  if p1 > p2.position.y:
    target=-p1+p2.position.y
  else:
    target=p2.position.y-p1
  return target



selectedLayer = Font.selectedLayers[0]
glyph=selectedLayer.parent

# for glyph in Font.glyphs:
for layer in glyph.layers:
  for path in layer.paths:
    for node in path.nodes:

      if(node.userData["anchors"]):
        
        for anchorName in node.userData["anchors"]:
          anchor=layer.anchors[anchorName]
          if(anchor):
            anchor.position=NSPoint(node.position.x,node.position.y)

      if(node.userData["distAnchors"]):
        
        for anchorName in node.userData["distAnchors"]:
          anchor=layer.anchors[anchorName]
          if(anchor):

            theta=math.radians( -angle ) 
            workerPointX=node.x*math.cos(theta)
            workerPointY=node.y*math.sin(theta)
            yTarget=getPt(workerPointY,node)

            anchor.x=getItalic(workerPointX,yTarget,angle)


            # anchor.position=NSPoint(node.position.x,node.position.y)

        

      
          

