#MenuTitle: Test
# -*- coding: utf-8 -*-
__doc__="""

Looks for kerning pairs and reduplicates their kerning for corresponding .sups glyphs, if they are available in the font.


"""
import GlyphsApp

# Glyphs.clearLog()
# Glyphs.showMacroWindow()
Font = Glyphs.font

selectedLayer = Font.selectedLayers[0]

smartGlyph=Font.glyphs["_part.serif"]
partsSettings=smartGlyph.partsSettings()

# for j in range(len(partsSettings)):
# 	name = partsSettings[j].name()
# 	minimum = partsSettings[j].bottomValue()
# 	maximum = partsSettings[j].topValue()
# 	pc=partsSettings[j].pieceComponent()
# 	print pc

# 	p=dir(partsSettings[j])

# 	# for pp in p:
# 	# 	print pp
# 	print "%s: from %f to %f" % ( name, minimum, maximum )





wValue=50
for comp in selectedLayer.components:
	properties = comp.pieceSettings()
	
	if properties != None :
		properties["B_Width"]=wValue
	else:
		comp.setPieceSettings_({"B_Width":wValue})


