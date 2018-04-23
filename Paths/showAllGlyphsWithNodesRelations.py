#MenuTitle: Show All Glyphs With Nodes Relations
# -*- coding: utf-8 -*-
__doc__="""
Show All Glyphs With Nodes Relations
"""

import GlyphsApp
import vanilla
import math

Glyphs.clearLog()
Glyphs.showMacroWindow()

Font = Glyphs.font

glyphNames=[]

for glyph in Font.glyphs:
  layer = glyph.layers[Font.selectedFontMaster.id]

  for path in layer.paths:
    for node in path.nodes:
      if node.name:
        glyphNames.append(glyph.name)
        break
    else:
      continue
    break

    
  # if layer.userData["NodesRelation"]:

    # for  key in layer.userData["NodesRelation"].keys():
    #   for item in layer.userData["NodesRelation"][key]:
    #     if item[:6]=="GSNode":
          
    #       del(layer.userData["NodesRelation"][key])
    #       break

    # glyphNames.append(glyph.name)

tabString = "/"+"/".join(glyphNames)
Font.newTab(tabString)


