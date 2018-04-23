#MenuTitle: Delete Nodes Relation
# -*- coding: utf-8 -*-
__doc__="""
Delete Nodes Relation
"""

import GlyphsApp
import uuid

Glyphs.clearLog()
Glyphs.showMacroWindow()


selectedLayer = Glyphs.font.selectedLayers[0]

selection = selectedLayer.selection


print selectedLayer.userData

if selection:
  for node in selection:
    if isinstance(node,GSNode):
      node.name=None
      del(node.userData["id"])

else:

  for path in selectedLayer.paths:
    for node in path.nodes:
      node.name=None
      del(node.userData["id"])
      
# for selectedPoint in selection:
#   selectedPoint.name=None


  if selectedLayer.userData["NodesRelation"]:
    for key in selectedLayer.userData["NodesRelation"].keys():
      del(selectedLayer.userData["NodesRelation"][key])
      # selectedLayer.userData["NodesRelation"]=None

  # if selectedLayer.userData.keys():
  #   for key in selectedLayer.userData.keys():
  #     print key
  #     del(selectedLayer.userData[key])

print selectedLayer.userData