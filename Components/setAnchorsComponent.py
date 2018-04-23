#MenuTitle: Set Anchors at component
# -*- coding: utf-8 -*-
__doc__="""
Set Anchors at component
"""

import GlyphsApp
import vanilla
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()


for l in Font.selectedLayers:

  for master in Font.masters:   
    glyph=l.parent
    # print master

    for comp in l.components:

      if(comp.rotation==0.0):
        if(comp.componentName=="_part.serif_left" or comp.componentName=="_part.serif_left.case" or comp.componentName=="_part.serif_right" or comp.componentName=="_part.serif_right.case"):

          comp.anchor="serif2"
          comp.userData["anchor"]=comp.anchor

      # print "%s : %s" % (comp.componentName,comp.anchor)
      # comp.userData["anchor"]="serif2"
       


    
    




