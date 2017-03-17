#MenuTitle: Bulk Kern Sups
# -*- coding: utf-8 -*-
__doc__="""

Bulk Kerning

"""
import GlyphsApp

Font = Glyphs.font
currMaster=Font.selectedFontMaster;
sups=[]
selectedLayers = Font.selectedLayers

# for glyph in Font.glyphs:
	# if ".sups" in glyph.name:
		# sups[]=glyph
# print sups


for thisLayer in selectedLayers:
	sourceGlyphName=thisLayer.parent.name  
	arr=sourceGlyphName.split(".")
	baseGlyphName=arr[0]
	print baseGlyphName