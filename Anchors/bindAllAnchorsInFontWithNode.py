#MenuTitle: Bind all anchors in a font with their node 
# -*- coding: utf-8 -*-
__doc__="""
Bind anchors with a node in a font. 
"""

import GlyphsApp
import vanilla
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()


selectedLayer = Font.selectedLayers[0]
# glyph=selectedLayer.parent

for glyph in Font.glyphs:
  for layer in glyph.layers:
    for path in layer.paths:
      for node in path.nodes:
        x=node.position.x
        y=node.position.y
        nodeAnchors=list()
        for anchor in layer.anchors:
          if(anchor.position.x==x and anchor.position.y==y):
            nodeAnchors.append(anchor.name)   

        if len(nodeAnchors)>0:
          node.userData["anchors"]=nodeAnchors
        else:
          del(node.userData["anchors"])
          

