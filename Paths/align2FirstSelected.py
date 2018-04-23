#MenuTitle: Align to first selected
# -*- coding: utf-8 -*-
__doc__="""
Aligns selection to the very first selected object (anchor, node, component) respecting italic angle
"""
import GlyphsApp
import math
Font = Glyphs.font

def getItalic(x, y, angle ):
	return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )

angle=float(Font.selectedFontMaster.italicAngle)
thisLayer = Font.selectedLayers[0]
selection= thisLayer.selection
first=selection[0]

for sel in  selection:

	if sel!=first: 
		

		if first.position.y>sel.position.y:
			y=-first.position.y + sel.position.y
		else:
			y=sel.position.y-first.position.y

		nP=getItalic(first.position.x,y,angle)#+85
		sel.position = NSPoint(nP,sel.position.y)
