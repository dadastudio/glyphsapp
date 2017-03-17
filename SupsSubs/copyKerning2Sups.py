#MenuTitle: Copy Kerning to .sups
# -*- coding: utf-8 -*-
__doc__="""

Looks for kerning pairs and reduplicates their kerning for corresponding .sups glyphs, if they are available in the font.


"""
import GlyphsApp

Font = Glyphs.font

# suffix="superior"
suffix=".sups"
currMaster=Font.selectedFontMaster;

kerning = Font.kerning[currMaster.id]
kerningToBeAdded = []

for k in kerning:

	baseGlyph=Font.glyphs[ k[7:]]

	supsGlyph=Font.glyphs[ k[7:]+suffix ]

	if supsGlyph!= None:


		# baseLeftKey = baseGlyph.leftKerningGroupId()
		# if baseLeftKey:
		# 	scLeftKey = baseLeftKey[:7] + baseLeftKey[7:]+suffix 
		# 	supsGlyph.setLeftKerningGroupId_(scLeftKey)


		# baseRightKey = baseGlyph.rightKerningGroupId()
		# if baseRightKey:
		# 	scRightKey = baseRightKey[:7] + baseRightKey[7:]+suffix 
		# 	supsGlyph.setRightKerningGroupId_(scRightKey)

		subLeftKey = k[:7]+k[7:]+suffix 
		
		scLeftKey=k[:7]

		for w in kerning[k]:
			
			supsGlyph2=Font.glyphs[ w[7:]+suffix ]


			if supsGlyph2!= None:

				scRightKey=w[:7]+w[7:]+suffix 
				value=kerning[k][w]
		
				kerningToBeAdded.append( (currMaster.id, subLeftKey, scRightKey, value) )


Font.disableUpdateInterface()
for thisKernInfo in kerningToBeAdded:
	fontMasterID = thisKernInfo[0]
	scLeftKey = thisKernInfo[1]
	scRightKey = thisKernInfo[2]
	scKernValue = thisKernInfo[3]
	Font.setKerningForPair( fontMasterID, scLeftKey, scRightKey, scKernValue )
Font.enableUpdateInterface()


