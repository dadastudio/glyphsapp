#MenuTitle: Steal SC Sidebearings from Caps
# -*- coding: utf-8 -*-
__doc__="""

Steal SC Sidebearings from Caps


"""
import GlyphsApp
import math
Font = Glyphs.font

# Glyphs.clearLog()
# Glyphs.showMacroWindow()
scaleFactor=.8

for layer in Font.selectedLayers:
  glyph=layer.parent
  print glyph.name[:-3]
  if glyph.name[-3:]==".sc":

    parent=Font.glyphs[glyph.name[:-3].upper()]

    if parent:

      if parent.leftMetricsKey:
        glyph.leftMetricsKey=parent.leftMetricsKey.lower()+".sc"
      else:        
        glyph.leftMetricsKey=None
        layer.LSB=parent.layers[Font.selectedFontMaster.id].LSB*scaleFactor

      if parent.rightMetricsKey:
        
        glyph.rightMetricsKey=parent.rightMetricsKey.lower()+".sc"

      else:        
        glyph.rightMetricsKey=None
        layer.RSB=parent.layers[Font.selectedFontMaster.id].RSB*scaleFactor


      layer.syncMetrics()
    else:
      print "Brak takiego glifa"
 