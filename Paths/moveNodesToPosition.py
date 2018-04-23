#MenuTitle: Move nodes to position
# -*- coding: utf-8 -*-
__doc__="""
Move nodes to position
"""
import GlyphsApp
Glyphs.clearLog()
Glyphs.showMacroWindow()


font = Glyphs.font

unrounded=505.209
rounded=506

for glyph in font.glyphs:
  layer=glyph.layers[font.selectedFontMaster.id]
  for path in layer.paths:
    for node in path.nodes: 

      if node.type==CURVE:
        if(round(node.position.y,3)==unrounded):
          node.position=NSPoint(node.x,rounded)

          print node


