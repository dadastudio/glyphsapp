#MenuTitle: Check Anchors
# -*- coding: utf-8 -*-
__doc__="""
check anchors across the font
"""

import GlyphsApp
Font = Glyphs.font


selectedLayers = Font.selectedLayers
Glyphs.clearLog()
Glyphs.showMacroWindow()

heights={"Light":460,"Regular":480,"Bold":514}
currText=""
master="Bold"
anchor="top"
Font.currentText=currText
for gl in Font.glyphs:

	if gl.subCategory=="Lowercase":

		for l in gl.layers:

			m=Font.masters[l.associatedMasterId]

			if m.name == master:
				if l.layerId == l.associatedMasterId: #only Master Layer
					if l.anchors[anchor]: # if anchor exists
						# print l
						if l.anchors["top"].y != heights[m.name]:
							currText=currText+" /"+gl.name
							print gl.name+": " +str(l.anchors["top"].y)


Font.currentText=currText
print currText
