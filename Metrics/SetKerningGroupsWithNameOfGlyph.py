#MenuTitle: Set kerning groups with name of a glyph
# -*- coding: utf-8 -*-
__doc__="""
Set kerning groups with name of a glyph
"""

import GlyphsApp

Font = Glyphs.font

for selectedLayer in Font.selectedLayers:
  glyph=selectedLayer.parent
  glyph.leftKerningGroup=glyph.name
  glyph.rightKerningGroup=glyph.name
