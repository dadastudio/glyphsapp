#MenuTitle: Sync Smart Components
# -*- coding: utf-8 -*-
__doc__="""

Sync Smart Components
"""

import GlyphsApp
import vanilla
import copy


Glyphs.clearLog()
Glyphs.showMacroWindow()

Font = Glyphs.font

for ff in Glyphs.fonts:
  if(ff==Font): continue

  if(ff.familyName==Font.familyName):
    Font2=ff

  else:
    print "Brak fonta o tej samej nazwie"




for selectedLayer in Font.selectedLayers:
  glyph=selectedLayer.parent


  if(Font2.glyphs[glyph.name]!=None):
     
    glyph2=Font2.glyphs[glyph.name]
    glyph.smartComponentAxes=copy.copy(glyph2.smartComponentAxes)

    for layer2 in glyph2.layers:
    
      if layer2.layerId != layer2.associatedMasterId:  #not master layer

        glyph.layers.append(copy.copy(layer2))

