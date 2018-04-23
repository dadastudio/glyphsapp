#MenuTitle: Copy Kerning to .sups
# -*- coding: utf-8 -*-
__doc__="""

Looks for kerning pairs and reduplicates their kerning for corresponding .sups glyphs, if they are available in the font.


"""
import GlyphsApp
import sys
Font = Glyphs.font

suffix=".sups"
currMaster=Font.selectedFontMaster;
figures=["zero.lf","one.lf","two.lf","three.lf","four.lf","five.lf","six.lf","seven.lf","eight.lf","nine.lf"]

kerning = Font.kerning[currMaster.id]
kerningToBeAdded = []

for k in kerning:

	baseGlyph=Font.glyphs[ k[7:]]
	# if baseGlyph: 
	# 	if baseGlyph.name in figures:
	# 		print baseGlyph.name

	# if baseGlyph.name in figures:
	# 	print baseGlyph.name

	#seven.lf > seven.sups

	if baseGlyph:
		if baseGlyph.name in figures:
			print k[7:]
			print baseGlyph.name[:-3]



			supsGlyph=Font.glyphs[ baseGlyph.name[:-3]+suffix ]

			print supsGlyph
		else:
			supsGlyph=Font.glyphs[ k[7:]+suffix ]
	else:
		continue



	if supsGlyph!= None:


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


