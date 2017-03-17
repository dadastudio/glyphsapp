#MenuTitle: Kern Questions Exclams Periods Ellipsis
# -*- coding: utf-8 -*-
__doc__="""

Test

"""
import GlyphsApp
import math
Font = Glyphs.font
# Glyphs.clearLog()
# Glyphs.showMacroWindow()

question=Font.glyphs["question"]
exclam=Font.glyphs["exclam"]
period=Font.glyphs["period"]
ellipsis=Font.glyphs["ellipsis"]


for thisMaster in Font.masters:

	questionLayer=question.layers[thisMaster.id]	
	periodLayer=period.layers[thisMaster.id]
	exclamLayer=exclam.layers[thisMaster.id]
	ellipsisLayer=ellipsis.layers[thisMaster.id]

	dotOffset=questionLayer.components[0].position.x
	exclamDotOffset=exclamLayer.components[0].position.x



	
	#...?
	Font.setKerningForPair(thisMaster.id,'@MMK_L_period','@MMK_R_question',round(-dotOffset))
	#?...	
	questionKern2= questionLayer.width-periodLayer.width-dotOffset
	Font.setKerningForPair(thisMaster.id,'@MMK_L_question','@MMK_R_period',round(-questionKern2))

	#...!
	exclamKern1=exclamLayer.components[0].x
	Font.setKerningForPair(thisMaster.id,'@MMK_L_period','@MMK_R_exclam',round(-exclamKern1))
	#!...
	exclamKern2= exclamLayer.width-periodLayer.width-exclamDotOffset
	Font.setKerningForPair(thisMaster.id,'@MMK_L_exclam','@MMK_R_period',round(-exclamKern2))

	#…?
	rc=ellipsisLayer.components[1].x-periodLayer.width

	Font.setKerningForPair(thisMaster.id,'ellipsis','question',round(-dotOffset+rc))
	#?…
	questionKern4= -questionKern2+rc #questionLayer.width-periodLayer.width-dotOffset-rc
	Font.setKerningForPair(thisMaster.id,'question','ellipsis',round(questionKern4))
	
	#…!
	rc=ellipsisLayer.components[1].x-periodLayer.width

	Font.setKerningForPair(thisMaster.id,'ellipsis','exclam',round(-exclamDotOffset+rc))
	#!…
	exclamKern4= exclamKern2-rc 
	Font.setKerningForPair(thisMaster.id,'exclam','ellipsis',round(-exclamKern4))
	









