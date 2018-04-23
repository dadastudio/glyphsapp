#MenuTitle: Copy anchors from one file to another
# -*- coding: utf-8 -*-
__doc__="""
Copy anchors from one file to another
"""

import GlyphsApp
import copy
Font = Glyphs.font
Font2 = Glyphs.fonts[1]

Glyphs.clearLog()
Glyphs.showMacroWindow()


selectedLayer = Font.selectedLayers[0]
glyph=selectedLayer.parent



glyphSrc=Font2.glyphs[glyph.name]


print glyphSrc.layers[0].anchors
print
print glyph.layers[0].anchors

# glyph.layers[0].anchors=copy.copy(glyphSrc.layers[0].anchors)


for layer in glyph.layers:

  layer.anchors=copy.copy(glyphSrc.layers[0].anchors)

  # print layer.anchors
 

# for layer in glyph.layers[0]:
#   print layer.anchors


# selectedLayer = Font.selectedLayers[0]
# glyph=selectedLayer.parent

