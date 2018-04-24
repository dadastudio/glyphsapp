#MenuTitle: Copy components
# -*- coding: utf-8 -*-
__doc__="""
Copy components from one file to another's background
"""

import GlyphsApp
import vanilla
import math


# Glyphs.clearLog()
# Glyphs.showMacroWindow()


Font = Glyphs.font

for ff in Glyphs.fonts:
  if(ff==Font): continue

  if(ff.familyName==Font.familyName):
    Font2=ff
    break
  else:
    print "Brak fonta o tej samej nazwie"



for selectedLayer in Font.selectedLayers:

  glyph=selectedLayer.parent

  if(Font2.glyphs[glyph.name]!=None):

    for m in range(len(Font.masters)):

      master=Font.masters[m]
      master2=Font2.masters[m]
      

      otherGlyph=Font2.glyphs[glyph.name]
      otherLayer=otherGlyph.layers[master2.id]

      glyph.beginUndo()

      mainLayer=glyph.layers[master.id]
      
      for i in range( len( mainLayer.paths ))[::-1]:
        del mainLayer.paths[i]

      mainLayer.anchors=copy.copy(otherLayer.anchors)
      mainLayer.components=copy.copy(otherLayer.components)
      mainLayer.LSB=otherLayer.LSB
      mainLayer.RSB=otherLayer.RSB
      mainLayer.syncMetrics()
      glyph.endUndo()




   
  