#MenuTitle: Remember Metrics
# -*- coding: utf-8 -*-
__doc__="""
Remember Metrics
"""

import GlyphsApp



Glyphs.clearLog()
Glyphs.showMacroWindow()

Font = Glyphs.font
selectedLayer = Font.selectedLayers[0]

for glyph in Font.glyphs:

  layer=glyph.layers[Font.selectedFontMaster.id]

  if not layer.userData["Metrics"]:
    layer.userData["Metrics"]={}

  layer.userData["Metrics"]["LSB"]=layer.LSB
  layer.userData["Metrics"]["RSB"]=layer.RSB



