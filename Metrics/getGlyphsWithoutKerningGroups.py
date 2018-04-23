#MenuTitle: Get glyphs without kerning groups
# -*- coding: utf-8 -*-
__doc__="""

Gets glyphs without kerning groups

"""
import GlyphsApp
import math
Font = Glyphs.font
Glyphs.clearLog()
Glyphs.showMacroWindow()
output=""
for g in Font.glyphs:
	if g.subCategory=="Uppercase" or g.subCategory=="Lowercase":
		
		if g.name.endswith(".subs"):
			continue


		LeftKey = g.leftKerningGroupId()
		RightKey = g.rightKerningGroupId()
		print g.name+" "+str(LeftKey)+" "+str(RightKey)
		if LeftKey==None and RightKey==None:
			output+="/"+g.name
		elif LeftKey==None:
			output+="/"+g.name
		elif RightKey==None:
			output+="/"+g.name

Font.newTab(output)