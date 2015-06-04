#MenuTitle: Test
# -*- coding: utf-8 -*-
__doc__="""
test
"""

import GlyphsApp
import vanilla
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()

for l in Font.selectedLayers:
	if l.anchors["origin"]:
		del(l.anchors["origin"])
		# print l.anchors["origin"]

		

