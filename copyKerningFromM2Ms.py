#MenuTitle: Copy kerning from M2Ms
# -*- coding: utf-8 -*-
__doc__="""

Copy kerning from selected Master to all Masters

"""
import GlyphsApp
Glyphs.clearLog()
Glyphs.showMacroWindow()

Font = Glyphs.font
masters=Font.masters
kerning = Font.kerning

currMaster=Font.selectedFontMaster;
currKerning=kerning[currMaster.id]

for m in masters:
	if m.id==currMaster.id:
		pass

	#Font.kerning[m.id]=currKerning
