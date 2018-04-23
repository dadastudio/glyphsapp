#MenuTitle: Set Nodes Relation
# -*- coding: utf-8 -*-
__doc__="""
Set Nodes Relation
"""

import GlyphsApp
import vanilla
import math
import random


# Glyphs.clearLog()
# Glyphs.showMacroWindow()

Font = Glyphs.font
selectedLayer = Font.selectedLayers[0]



def getItalic(x, y, angle ):
  return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )

def getPt(p1,p2):

  if p1 > p2.position.y:
    target=-p1+p2.position.y
  else:
    target=p2.position.y-p1
  return target


def getNode(nodeId):
  #print "getNode"
  for path in selectedLayer.paths:
    for node in path.nodes:

      if node.userData["id"]:

        if nodeId==node.userData["id"]:
          # print "------------------"
          return node


allSell=[]

for mainNodeId in selectedLayer.userData["NodesRelation"].keys():
  print ("mainNodeId "+mainNodeId)
  selection=[]
  gn=getNode(mainNodeId)
  selection.append(getNode(mainNodeId))

  for secNodeId in selectedLayer.userData["NodesRelation"][mainNodeId]:
    selection.append(getNode(secNodeId))
  
  allSell.append(selection)

# print allSell
master=Font.selectedFontMaster
if master.name=="Light":
  r=5
elif master.name=="Regular":

  r=10
else:
  r=15



  
# r=random.randrange(5,20)

def movePoints(selection):

  firstPoint=selection[0]
  secondPoint=selection[1]


  print firstPoint
  print secondPoint
  
  theta = math.atan2(secondPoint.y - firstPoint.y, secondPoint.x - firstPoint.x) #radians
  angle=float(90-math.degrees(theta))#math.degrees(theta) #degrees

  offset=0
  for selectedPoint in  selection:

    if selectedPoint==None:
      continue

    if selectedPoint!=firstPoint and selectedPoint!=secondPoint: 

      theta=( -angle / 180 ) * math.pi 

      workerPointX=firstPoint.x+r*math.cos(theta)
      workerPointY=firstPoint.y+r*math.sin(theta)

      yTarget=getPt(workerPointY,selectedPoint)

      selectedPoint.x=getItalic(workerPointX,yTarget,angle)+offset

      if selectedPoint.smooth:

        if selectedPoint.nextNode.type==OFFCURVE:
          offPt=getPt(workerPointY,selectedPoint.nextNode)
          selectedPoint.nextNode.x=getItalic(workerPointX,offPt,angle)+offset
        if selectedPoint.prevNode.type==OFFCURVE:
          offPt=getPt(workerPointY,selectedPoint.prevNode)
          selectedPoint.prevNode.x=getItalic(workerPointX,offPt,angle)+offset



for s in allSell:
  
  movePoints(s)

