#MenuTitle: Show Smart Components
# -*- coding: utf-8 -*-
__doc__="""

Show Smart Components
"""

import GlyphsApp


Glyphs.clearLog()
Glyphs.showMacroWindow()

Font = Glyphs.font


glyphList=[]
for glyph in Font.glyphs:

  if len(glyph.smartComponentAxes)>0:

    gn=glyph.name
    glyphList.append(glyph.name)

    # glyph.name=gn.replace("_part","_smart")
    print glyph


if glyphList:
  tabString = "/"+"/".join(glyphList)
  Font.newTab(tabString)
else:
  print "No Smart Components"  
