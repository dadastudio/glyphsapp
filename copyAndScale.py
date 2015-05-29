#MenuTitle: Makes copies with suffix
# -*- coding: utf-8 -*-
__doc__="""
Goes through all selected glyphs, makes copy and adds suffix
"""

import GlyphsApp
Font = Glyphs.font

selectedLayers = Font.selectedLayers
Glyphs.clearLog()
Glyphs.showMacroWindow()

# SMALL CAPS

offset=0
suffix=".sc"
sideBearingFactor=0
scaleFactors=[.78,.82,.88]
makeLowercase=True
baseName=True

# SUPERSCRIPT

# offset=250
# suffix=".sups"
# sideBearingFactor=.9
# scaleFactors=[.6,.6,.6]
# makeLowercase=False
# removeAnchors=True

# SUBSCRIPT

# offset=-150
# suffix=".subs"
# sideBearingFactor=.9
# scaleFactors=[.6,.6,.6]
# makeLowercase=False
# removeAnchors=True
targetGlyph
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

	if makeLowercase :
		pf=sourceGlyphName.split(".")
		pf[0]= pf[0].lower()		
		newGlyphName=""
		for x in pf:
			newGlyphName=newGlyphName + "." + x	

		newGlyphName = newGlyphName[1:len(newGlyphName)] + suffix

	else:
		newGlyphName=sourceGlyphName + suffix
	
	if baseName:
		pf=sourceGlyphName.split(".")
		newGlyphName=pf[0] + suffix

	if Font.glyphs[newGlyphName]:		

		targetGlyph=Font.glyphs[newGlyphName]
	else:		
		targetGlyph = GSGlyph( newGlyphName )
		Font.glyphs.append( targetGlyph )

	i=0	
	for thisMaster in Font.masters:		

		sourceLayer=sourceGlyph.layers[thisMaster.id]		
		
		targetGlyph.layers[thisMaster.id]=sourceLayer.copyDecomposedLayer()
		layer=targetGlyph.layers[thisMaster.id]

		transformNodes( layer, scaleFactors[i] )

		
		if removeAnchors == True:
			layer.setAnchors_( None )
			
		
		if sideBearingFactor == 1 :
			layer.setLeftMetricsKey_(sourceGlyph.name) 
			layer.setRightMetricsKey_(sourceGlyph.name) 
		elif sideBearingFactor == 0 :
			layer.setLeftMetricsKey_(sourceGlyph.name+"*"+str(scaleFactors[i])) 
			layer.setRightMetricsKey_(sourceGlyph.name+"*"+str(scaleFactors[i])) 

		else :
			layer.setLeftMetricsKey_(sourceGlyph.name+"*"+str(sideBearingFactor)) 
			layer.setRightMetricsKey_(sourceGlyph.name+"*"+str(sideBearingFactor)) 
			
			
		layer.syncMetrics()
		
		
		i=i+1


Font.enableUpdateInterface() 


