#MenuTitle: Remember Nodes Relation
# -*- coding: utf-8 -*-
__doc__="""
Remember Nodes Relation
"""

import GlyphsApp
import uuid

Glyphs.clearLog()
Glyphs.showMacroWindow()


selectedLayer = Glyphs.font.selectedLayers[0]
selection = selectedLayer.selection

def getId():
  return str(uuid.uuid4())


firstPoint=selection[0]

if firstPoint.name==None:
  uid=getId()
  firstPoint.name="NR"
  firstPoint.userData["id"]=uid

others=[]

selc=selection[1:]
# print selc
for i in range(len(selc)):

  selectedPoint=selc[i]
  selectedPoint.name=str(i)
  uid=getId()
  selectedPoint.userData["id"]=uid
  # print i
  print selectedPoint

  others.append(uid)
  # print selectedPoint.name




# print selectedLayer.selection[2].name
# print selectedLayer.selection[3].name


# print "others"
# print others

for selectedPoint in selection:
  print selectedPoint.userData

if selectedLayer.userData["NodesRelation"]==None:
  selectedLayer.userData["NodesRelation"]={}

selectedLayer.userData["NodesRelation"][firstPoint.userData["id"]]=others

# print selectedLayer.userData
