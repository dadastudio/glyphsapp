#MenuTitle: Position UC marks
# -*- coding: utf-8 -*-
__doc__="""
Position UC marks
"""
import GlyphsApp
import math
import copy
Font = Glyphs.font


# Glyphs.clearLog()
# Glyphs.showMacroWindow()

_topY=700

if Font.selectedFontMaster.name.startswith("Light") :
	topY=880
elif Font.selectedFontMaster.name.startswith("Regular"):
	topY=900
elif Font.selectedFontMaster.name.startswith("Bold"):
	topY=930
angle=float(Font.selectedFontMaster.italicAngle) #8.0
	
caseOffset=180


caseSuffix=".case"


def getItalic(x, y, angle ):
	return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )

theta=math.radians(angle)

for thisLayer in Font.selectedLayers:

	try:
		
		ucGlyph=Font.glyphs[thisLayer.parent.name+caseSuffix]
		layer = ucGlyph.layers[Font.selectedFontMaster.id]

		layer.anchors = copy.copy(thisLayer.anchors)

		# layer.setLeftMetricsKey_(thisLayer.parent.name) 
		# layer.setRightMetricsKey_(thisLayer.parent.name) 

		comp=layer.components[0]
		compX= getItalic(0, caseOffset, angle )
		comp.position=NSPoint(compX,caseOffset)

		posX=thisLayer.anchors["_top"].position.x

		if(layer.anchors["_top"]):
			_topAnchor=layer.anchors["_top"]
			x=getItalic(_topAnchor.position.x,_topY-_topAnchor.position.y,angle)	
			_topAnchor.position=NSPoint(x,_topY)

		if(layer.anchors["top"]):
			topAnchor=layer.anchors["top"]
			x=getItalic(topAnchor.position.x,topY-topAnchor.position.y,angle)	

			topAnchor.position=NSPoint(x,topAnchor.position.y+caseOffset)


		# layer.syncMetrics()

		pass
	except Exception, e:
		print e

