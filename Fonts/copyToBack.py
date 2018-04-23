#MenuTitle: Copy to background
# -*- coding: utf-8 -*-
__doc__="""
Copy glyph from one file to another's background
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


xOffset=0
scaleFactor=.925


def skewPaths(layer,angle):
  for path in layer.paths:

    path.applyTransform([
      
      scaleFactor,  # x scale factor
      0.0,          # x skew factor
      angle,        # y skew factor
      1.0,          # y scale factor
      0.0,      # x position
      0.0           # y position
      ])

  for anchor in layer.anchors:
    anchor.x=anchor.x + ( anchor.y * math.tan(angle) )




for selectedLayer in Font.selectedLayers:

  glyph=selectedLayer.parent

  if(Font2.glyphs[glyph.name]!=None):

    for m in range(len(Font.masters)):

      master=Font.masters[m]
      master2=Font2.masters[m]
      
      angle=math.radians( master.italicAngle ) 

      otherGlyph=Font2.glyphs[glyph.name]
      otherLayer=otherGlyph.layers[master2.id]

      # glyph.layers[master.id]=otherLayer.copyDecomposedLayer()
      mainLayer=glyph.layers[master.id]

      glyph.layers[master.id].background=otherLayer.copyDecomposedLayer()
      background=glyph.layers[master.id].background

      

      # skewPaths(mainLayer,angle)
      skewPaths(background,angle)
      # background.addNodesAtExtremes()
      # background.LSB=otherLayer.LSB*scaleFactor
      # background.syncMetrics()
 
      # background.addNodesAtExtremes()
      # background.LSB=otherLayer.LSB*scaleFactor

      # mainLayer.LSB=round(otherLayer.LSB*scaleFactor)
      # mainLayer.RSB=round(otherLayer.RSB*scaleFactor)

   
  