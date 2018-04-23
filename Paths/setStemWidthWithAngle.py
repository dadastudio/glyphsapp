#MenuTitle: Set Stem Width at Angle
# -*- coding: utf-8 -*-
__doc__="""
Set Stem Width at Angle
"""

import GlyphsApp
import vanilla
import math
Font = Glyphs.font
selectedLayer = Font.selectedLayers[0]
glyph=selectedLayer.parent

# verticalStems=Font.selectedFontMaster.verticalStems
# horizontalStems=Font.selectedFontMaster.horizontalStems

# if glyph.subCategory=="Uppercase":
#   r=horizontalStems[1]
# else:
#   r=horizontalStems[0]

def getItalic(x, y, angle ):
  return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )

def getPt(p1,p2):

  if p1 > p2.position.y:
    target=-p1+p2.position.y
  else:
    target=p2.position.y-p1
  return target


selection = selectedLayer.selection

firstPoint=selection[0]
secondPoint=selection[1]

theta = math.atan2(secondPoint.y - firstPoint.y, secondPoint.x - firstPoint.x) #radians
angle=float(90-math.degrees(theta))#math.degrees(theta) #degrees


r=110



offset=0

for selectedPoint in  selection:

  if selectedPoint!=firstPoint and selectedPoint!=secondPoint: 

    theta=( -angle / 180 ) * math.pi 

    workerPointX=firstPoint.x+r*math.cos(theta)
    workerPointY=firstPoint.y+r*math.sin(theta)

    yTarget=getPt(workerPointY,selectedPoint)

    selectedPoint.x=getItalic(workerPointX,yTarget,angle)+offset

    # selectedPoint.x=workerPointX
    # selectedPoint.y=workerPointY

    if selectedPoint.smooth:

      if selectedPoint.nextNode.type==OFFCURVE:
        offPt=getPt(workerPointY,selectedPoint.nextNode)
        selectedPoint.nextNode.x=getItalic(workerPointX,offPt,angle)+offset
      if selectedPoint.prevNode.type==OFFCURVE:
        offPt=getPt(workerPointY,selectedPoint.prevNode)
        selectedPoint.prevNode.x=getItalic(workerPointX,offPt,angle)+offset







# theta = math.atan2(secondPoint.y - firstPoint.y, secondPoint.x - firstPoint.x);

# theta=( -theta / 180 ) * math.pi 

# workerPointX=firstPoint.x+r*math.cos(theta)
# workerPointY=firstPoint.y+r*math.sin(theta)


# selectedPoint.y=workerPointY
# angleRadians = math.atan2(firstPoint.y - secondPoint.y, firstPoint.x - secondPoint.x);
# yTarget=getPt(workerPointY,thirdPoint)

# thirdPoint.x=getItalic(workerPointX,yTarget,angle)+offset
  