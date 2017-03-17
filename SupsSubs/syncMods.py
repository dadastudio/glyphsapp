#MenuTitle: Sync Mods
# -*- coding: utf-8 -*-
__doc__="""

Syncs mods

"""
import GlyphsApp
import math

#Glyphs.clearLog()
#Glyphs.showMacroWindow()

Font = Glyphs.font

#mods=("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",  "r", "s", "t", "u", "v", "w", "x", "y", "z")

mods=("a","b","c","d","e","f","g","k","m","o","p","t","u","v","z")
superiors=("h","i","j","l","n","r","s","w","x","y","plus","minus","equal","parenleft","parenright")

#superiors=("plus","minus","equal","parenleft","parenright")
modSuffix="superior"

selectedLayers = Font.selectedLayers

for thisLayer in selectedLayers:

	sourceGlyphName=thisLayer.parent.name  
	
	if sourceGlyphName in mods: # creates superscript glyph (eg. lmod) with unicode value
			
		if Font.glyphs[sourceGlyphName+modSuffix]==None:
			Font.glyphs.append( GSGlyph( sourceGlyphName+modSuffix ) )

		modGlyph=Font.glyphs[sourceGlyphName+modSuffix]
		for modMaster in Font.masters:
			
			modLayer=modGlyph.layers[modMaster.id]

			modLayer.components=[]
			modLayer.paths=[]
			modLayer.anchors=[]

			modLayer.components.append(GSComponent(sourceGlyphName+".sups"))
			# setKerningGroups(sourceGlyphName,sourceGlyphName+"mod")
			# setSidebearings(sourceGlyphName,targetGlyphName)			
