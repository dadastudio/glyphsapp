#MenuTitle: Position components on their anchors
# -*- coding: utf-8 -*-
__doc__="""
Position components on their anchors
"""

import GlyphsApp
import vanilla
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()


for l in Font.selectedLayers:


  for comp in l.components:


    if(comp.anchor!=None):
 
      comp.anchor=comp.userData["anchor"]
    else:
      comp.anchor="serif1"
      comp.userData["anchor"]="serif1"

       
