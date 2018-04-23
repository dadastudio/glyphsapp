#MenuTitle: Recreate Path
# -*- coding: utf-8 -*-
__doc__="""
Recreate Path
"""

import GlyphsApp
import vanilla
import math

Glyphs.clearLog()
Glyphs.showMacroWindow()

Font = Glyphs.font
selectedLayer = Glyphs.font.selectedLayers[0]

selection = selectedLayer.selection


def cloneNodes(path):
  newNodes=[]
  for node in path.nodes:
    if isinstance(node,GSNode):
      newNode=GSNode()
      newNode.position=NSPoint(node.x+100,node.y)
      newNode.type=node.type
      newNode.connection=node.connection

      newNodes.append(newNode)

  return newNodes

# Font.disableUpdateInterface()


newPaths=[]
for i in range(len(selectedLayer.paths)):
  path=selectedLayer.paths[i]
  
  if path.selected:    
    
    newPath=GSPath()
    newPath.nodes=cloneNodes(path)
    newPath.closed=True    
    newPaths.append(newPath)
    




# r=range(len(selectedLayer.paths))
selectedLayer.parent.beginUndo()
for i in range(len(selectedLayer.paths))[::-1]:

  path=selectedLayer.paths[i]

  if path.selected:
    del(selectedLayer.paths[i])

selectedLayer.parent.endUndo()
Font.enableUpdateInterface()

for newPath in newPaths:
  selectedLayer.paths.append(newPath)
    