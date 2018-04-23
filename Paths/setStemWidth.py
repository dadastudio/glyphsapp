#MenuTitle: Set Stem Width
# -*- coding: utf-8 -*-
__doc__="""
Sets stem width
"""

import GlyphsApp
import vanilla
import math

# Glyphs.clearLog()
# Glyphs.showMacroWindow()



Font = Glyphs.font
verticalStems=Font.selectedFontMaster.verticalStems
angle=float(Font.selectedFontMaster.italicAngle)


def getPt(p1,p2):

  if p1 > p2.position.y:
    target=-p1+p2.position.y
  else:
    target=p2.position.y-p1
  return target

def getItalic(x, y, angle ):
  return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )

selectedLayer = Font.selectedLayers[0]
glyph=selectedLayer.parent
selection = selectedLayer.selection
glyph.storeSubCategory=True

if glyph.subCategory=="Uppercase":
  r=verticalStems[1]
else:
  r=verticalStems[0]

r=0
offset=0

firstPoint=selection[0]

for selectedPoint in  selection:

  if selectedPoint!=firstPoint: 

    theta=math.radians( -angle ) 

    workerPointX=firstPoint.x+r*math.cos(theta)
    workerPointY=firstPoint.y+r*math.sin(theta)

    yTarget=getPt(workerPointY,selectedPoint)

    selectedPoint.x=getItalic(workerPointX,yTarget,angle)+offset

    if isinstance(selectedPoint,GSNode) and selectedPoint.smooth:

      if selectedPoint.nextNode.type==OFFCURVE:
        offPt=getPt(workerPointY,selectedPoint.nextNode)
        selectedPoint.nextNode.x=getItalic(workerPointX,offPt,angle)+offset
      if selectedPoint.prevNode.type==OFFCURVE:
        offPt=getPt(workerPointY,selectedPoint.prevNode)
        selectedPoint.prevNode.x=getItalic(workerPointX,offPt,angle)+offset


    # selectedPoint.x=firstPoint.x+r*math.cos(theta)
    # selectedPoint.y=firstPoint.y+r*math.sin(theta)

  # selectedPoint.y=workerPointY
  # angleRadians = math.atan2(selectedPoint.y - firstPoint.y, selectedPoint.x - firstPoint.x);
  # angleRadians = math.atan2(firstPoint.y - selectedPoint.y, firstPoint.x - selectedPoint.x);

  # selectedPoint.x=firstPoint.x+r*math.cos(angleRadians)
  # selectedPoint.y=firstPoint.y+r*math.sin(angleRadians)
  
