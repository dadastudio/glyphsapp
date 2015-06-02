#MenuTitle: Test
# -*- coding: utf-8 -*-
__doc__="""
test
"""

import GlyphsApp
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()


selectedLayers = Font.selectedLayers
Glyphs.clearLog()
Glyphs.showMacroWindow()

# sourceGlyph=GSGlyph( "A" )
# targetGlyph = GSGlyph( "A.ss01" )
# targetGlyph=sourceGlyph.copy()
# Font.glyphs.append( targetGlyph )

heights={"Light":460,"Regular":480,"Bold":514}

for gl in Font.glyphs:

	
	for l in gl.layers:

		m=l.associatedMasterId	
		if l.anchors["top"].y != 460:
		print targetGlyph.name+": " + str(thisLayer.anchors["top"].y)
	
		# if l.anchors["top"].y != heights["Regular"]:
		# print targetGlyph.name+": " + str(thisLayer.anchors["top"].y)

		print l

Font.currentText="a"
# for thisLayer in selectedLayers:
	
# 	sourceGlyphName=thisLayer.parent.name  
	
# 	targetGlyph=Font.glyphs[sourceGlyphName]
# 	if thisLayer.anchors["top"].y != 460:
# 		print targetGlyph.name+": " + str(thisLayer.anchors["top"].y)
		
