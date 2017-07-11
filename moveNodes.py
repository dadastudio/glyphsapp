#MenuTitle: Move selected nodes to zero position 
# -*- coding: utf-8 -*-
__doc__="""
Move selected nodes to zero position
"""
import GlyphsApp


Font = Glyphs.font

selectedLayer = Font.selectedLayers[0]

for path in selectedLayer.paths:
  for node in path.nodes: 
    if node.selected:
      if node.type==OFFCURVE:

        if node.prevNode.type==LINE:
          node.position=node.prevNode.position
        if node.nextNode.type==CURVE:
          node.position=node.nextNode.position

        