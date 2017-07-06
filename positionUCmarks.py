#MenuTitle: Position UC marks
# -*- coding: utf-8 -*-
__doc__="""
Position UC marks
"""
import GlyphsApp
import math
Font = Glyphs.font


# Glyphs.clearLog()
# Glyphs.showMacroWindow()

def getItalic(x, y, angle ):
	return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )

thisLayer = Font.selectedLayers[0]
_topY=700



if Font.selectedFontMaster.name.startswith("Light") :
	topY=880
elif Font.selectedFontMaster.name.startswith("Regular"):
	topY=900
elif Font.selectedFontMaster.name.startswith("Bold"):
	topY=930

angle=Font.selectedFontMaster.italicAngle #8.0
caseOffset=170
# caseOffset=138

caseSuffix=".case"
try:
	
	ucGlyph=Font.glyphs[thisLayer.parent.name+caseSuffix]
	layer = ucGlyph.layers[Font.selectedFontMaster.id]
	
	comp=layer.components[0]
	compX= getItalic(0, caseOffset, angle )
	comp.position=NSPoint(compX,caseOffset)

	for a in thisLayer.anchors:
		if(layer.anchors[a.name]):
			aCase=layer.anchors[a.name]

			if(a.name=="_top"):
				y=_topY
			elif(a.name=="top"):
				y=topY
			x=getItalic(a.position.x,aCase.position.y -a.position.y,angle)		
			layer.anchors[a.name].position=NSPoint(x,y)


	pass
except Exception, e:
	print e
	raise e

