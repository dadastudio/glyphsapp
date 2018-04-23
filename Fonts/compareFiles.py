#MenuTitle: Compare glyphs in files
# -*- coding: utf-8 -*-
__doc__="""
Compare glyphs in files
"""

import GlyphsApp
import vanilla
import math

Glyphs.clearLog()
Glyphs.showMacroWindow()


Font = Glyphs.font
Font2 = Glyphs.fonts[1]

# Fonts = Glyphs.fonts
print Font
print Font2

for i in range(len(Font.glyphs)):

  glyph=Font.glyphs[i]

  if(Font2.glyphs[glyph.name]==None):
    newGlyph = Font.glyphs[glyph.name].copy()
    Font2.glyphs.append(newGlyph)
    print glyph.name
    # break


  