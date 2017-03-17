#MenuTitle: Syncs kerning groups
# -*- coding: utf-8 -*-
__doc__="""



"""
import GlyphsApp

Font = Glyphs.font
suffix=".sups"
for glyph in Font.glyphs:

	supGlyph=Font.glyphs[glyph.name+suffix]

	if supGlyph!= None:
		
		baseLeftKey = glyph.leftKerningGroupId()
		if baseLeftKey:
			scLeftKey = baseLeftKey[:7] + baseLeftKey[7:]+suffix 
			supGlyph.setLeftKerningGroupId_(scLeftKey)


		baseRightKey = glyph.rightKerningGroupId()
		if baseRightKey:
			scRightKey = baseRightKey[:7] + baseRightKey[7:]+suffix 
			supGlyph.setRightKerningGroupId_(scRightKey)
			
	