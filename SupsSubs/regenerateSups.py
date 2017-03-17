#MenuTitle: Regenerate Superscript
# -*- coding: utf-8 -*-
__doc__="""


"""

import GlyphsApp
import vanilla


Font = Glyphs.font
sideBearingFactor=0.9

def transformNodes( thisLayer , sf ):
	offset=700	
	
	xHeight= Font.selectedFontMaster.xHeight * sf
	offset-=xHeight/2

	for thisPath in thisLayer.paths:
		for thisNode in thisPath.nodes:

			pos = thisNode.position
			pos.x = pos.x * sf
			pos.y = pos.y * sf
			thisNode.position = pos

			thisNode.y += offset
			
Font.disableUpdateInterface() 

for glyph in Font.glyphs:

	if glyph.name.endswith(".sups"):
	
		baseName=glyph.name[:-5]

		baseGlyph=Font.glyphs[baseName]
		
		for master in Font.masters:
			layer = baseGlyph.layers[master.id]
			supLayer=glyph.layers[master.id]
			glyph.layers[master.id]=layer.copyDecomposedLayer()

			transformNodes( glyph.layers[master.id] , 0.6 )

			glyph.layers[master.id].setLeftMetricsKey_(baseGlyph.name+"*"+str(sideBearingFactor)) 
			glyph.layers[master.id].setRightMetricsKey_(baseGlyph.name+"*"+str(sideBearingFactor)) 

			glyph.layers[master.id].setAnchors_( None )

			glyph.layers[master.id].syncMetrics()

Font.enableUpdateInterface()




			