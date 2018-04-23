#MenuTitle: Set color label on glyphs without kerning groups
# -*- coding: utf-8 -*-
__doc__="""
new Tab with glyphs withour kerning group set
"""

import GlyphsApp
import vanilla
import math
Font = Glyphs.font
selectedLayer = Font.selectedLayers[0]
g=selectedLayer.parent
Glyphs.clearLog()
Glyphs.showMacroWindow()

glyphNames=[]

# for g in Font.glyphs:
for g in Font.glyphs:
  

  if not g.export or g.name[:1]=="_":
    continue


  if not g.rightKerningGroup or not g.leftKerningGroup:
    glyphNames.append(g.name)
    g.color=9
  else:
    g.color=9223372036854775807
  

# tabString = "/"+"/".join(glyphNames)
# Font.newTab(tabString)