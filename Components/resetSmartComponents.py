#MenuTitle: Reset Smart Components
# -*- coding: utf-8 -*-
__doc__="""
Reset Smart Components
"""

import GlyphsApp
import vanilla
Font = Glyphs.font


for selectedLayer in Font.selectedLayers:

  for component in selectedLayer.components:
     
    glyph=component.component
    layer=glyph.layers[Font.selectedFontMaster.id]




    for axe in glyph.smartComponentAxes: 

      if layer.smartComponentPoleMapping[axe.name]==1:
        component.smartComponentValues[axe.name]=axe.bottomValue
      else:
        component.smartComponentValues[axe.name]=axe.topValue


