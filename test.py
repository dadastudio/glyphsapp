#MenuTitle: Test
# -*- coding: utf-8 -*-
__doc__="""
test
"""

import GlyphsApp
Font = Glyphs.font

selectedLayers = Font.selectedLayers
Glyphs.clearLog()
Glyphs.showMacroWindow()

for thisLayer in selectedLayers:
	
	# sourceGlyphName=thisLayer.parent.name  
	# sourceGlyph=Font.glyphs[sourceGlyphName]
	thisLayer.syncMetrics()