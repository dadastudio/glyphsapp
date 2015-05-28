#MenuTitle: Makes copies with suffix
# -*- coding: utf-8 -*-
__doc__="""
Goes through all selected glyphs, makes copy and adds suffix
"""

import GlyphsApp
Font = Glyphs.font

selectedLayers = Font.selectedLayers
# Glyphs.clearLog()
# Glyphs.showMacroWindow()

# SMALL CAPS

# offset=0
# suffix=".sc"
# sideBearingFactor=0
# scaleFactors=[.78,.82,.88]
# makeLowercase=True


# SUPERSCRIPT

offset=250
suffix=".sups"
sideBearingFactor=.9
scaleFactors=[.6,.6,.6]
makeLowercase=False


def transformNodes( thisLayer , sf ):
	
	for thisPath in thisLayer.paths:
		for thisNode in thisPath.nodes:

			pos = thisNode.position
			pos.x = pos.x * sf
			pos.y = pos.y * sf
			thisNode.position = pos

			thisNode.y += offset

	for thisAnchor in thisLayer.anchors:
		apos=thisAnchor.position
		apos.x=apos.x * sf
		apos.y=apos.y * sf + offset
		thisAnchor.position=apos

			
Font.disableUpdateInterface() 

for thisLayer in selectedLayers:
	
	sourceGlyphName=thisLayer.parent.name  
	sourceGlyph=Font.glyphs[sourceGlyphName]

	# newGlyphName=sourceGlyphName + suffix
	
	if makeLowercase :
		pf=sourceGlyphName.split(".")
		pf[0]= pf[0].lower()		
		newGlyphName=""
		for x in pf:
			newGlyphName=newGlyphName + "." + x	

		newGlyphName = newGlyphName[1:len(newGlyphName)] + suffix

	else:
		newGlyphName=sourceGlyphName + suffix

	if Font.glyphs[newGlyphName]:		
		targetGlyph=Font.glyphs[newGlyphName]
	else:		
		targetGlyph = GSGlyph( newGlyphName )
		Font.glyphs.append( targetGlyph )

	i=0	
	for thisMaster in Font.masters:		

		sourceLayer=sourceGlyph.layers[thisMaster.id]		
		
		# thisGlyph = thisLayer.parent
		# thisGlyphInfo = GSGlyphsInfo.glyphInfoForGlyph_( sourceGlyph )
		# print thisGlyphInfo

		# targetGlyph.layers[thisMaster.id].paths=[]
		# targetGlyph.layers[thisMaster.id].components=[]
		# targetGlyph.layers[thisMaster.id].anchors=[]
		# targetGlyph.layers[thisMaster.id].setComponents_( None )

		targetGlyph.layers[thisMaster.id]=sourceLayer.copyDecomposedLayer()
		layer=targetGlyph.layers[thisMaster.id]
		
		transformNodes( layer, scaleFactors[i] )

		#layer.correctPathDirection()

		
		if sideBearingFactor == 1 :
			targetGlyph.leftMetricsKey=sourceGlyph.name
			targetGlyph.rightMetricsKey=sourceGlyph.name
		elif sideBearingFactor == 0 :

			targetGlyph.leftMetricsKey="="+sourceGlyph.name+"*"+str(scaleFactors[i])
			targetGlyph.rightMetricsKey="="+sourceGlyph.name+"*"+str(scaleFactors[i])

		else :

			targetGlyph.leftMetricsKey="="+sourceGlyph.name+"*"+str(sideBearingFactor)
			targetGlyph.rightMetricsKey="="+sourceGlyph.name+"*"+str(sideBearingFactor)

		layer.syncMetrics()
		
		i=i+1


Font.enableUpdateInterface() 


