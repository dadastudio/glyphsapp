#MenuTitle: Remember components anchors
# -*- coding: utf-8 -*-
__doc__="""
Remember components anchors
"""

import GlyphsApp
import vanilla
Font = Glyphs.font

for glyph in Font.glyphs:

  for layer in glyph.layers:

    for comp in layer.components:
      if comp.anchor:
        comp.userData["anchor"]=comp.anchor
       

    
    




