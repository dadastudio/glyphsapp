#MenuTitle: Show Sups And UC 
# -*- coding: utf-8 -*-
__doc__="""

Shows Sups and UC counterparts of selected glyphs

"""
import GlyphsApp
Glyphs.clearLog()
Glyphs.showMacroWindow()

Font = Glyphs.font


currMaster=Font.selectedFontMaster;

string=""
stringSups=""
stringSC=""



selectedLayers = Font.selectedLayers

for layer in selectedLayers:
	string+=" /"+layer.parent.name
	stringSups+=" /"+layer.parent.name+".sups"
	stringSC+=" /"+layer.parent.name.lower()+".sc"
	




Font.currentText=string[1:]+"\n\n"+stringSups[1:]+"\n\n"+stringSC[1:]
# Font.newTab(output)

