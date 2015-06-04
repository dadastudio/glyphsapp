#MenuTitle: Position anchors on int
# -*- coding: utf-8 -*-
__doc__="""
Position anchors on int
"""

import GlyphsApp
import vanilla
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()


for l in Font.selectedLayers:

	for master in Font.masters:		
		glyph=l.parent
		layer=glyph.layers[master.id]

		for a in layer.anchors:
			
			a.x=int(a.x)
			a.y=int(a.y)
		




